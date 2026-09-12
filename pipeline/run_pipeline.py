import sys
import os
import argparse
import glob
import subprocess

def map_filename_to_subject(filename):
    name = filename.lower()
    if 'toan' in name:
        return 'toan'
    elif 'ngu-van' in name or 'nguvan' in name:
        return 'ngu-van'
    elif 'khoa-hoc' in name or 'khtn' in name:
        return 'khtn'
    elif 'tieng-anh' in name:
        return 'tieng-anh'
    return 'unknown'

def main():
    parser = argparse.ArgumentParser(description="Orchestrate the AI pipeline for SGK.")
    parser.add_argument('--grade', required=True, help="Grade number (e.g. 6)")
    parser.add_argument('--data-dir', required=True, help="Directory containing PDF files")
    parser.add_argument('--output-dir', required=True, help="Directory to save generated web content")
    parser.add_argument('--dry-run', action='store_true', help="Print commands without executing")

    args = parser.parse_args()
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    extract_script = os.path.join(script_dir, 'extract_pdf.py')
    generate_script = os.path.join(script_dir, 'generate_content.py')
    
    # Create temp directory for extracted json
    temp_extract_dir = os.path.join(script_dir, 'temp_extracted')
    if not args.dry_run:
        os.makedirs(temp_extract_dir, exist_ok=True)
        os.makedirs(args.output_dir, exist_ok=True)
        
    pdf_pattern = os.path.join(args.data_dir, f"**/*{args.grade}*.pdf")
    pdf_files = glob.glob(pdf_pattern, recursive=True)
    
    if not pdf_files:
        print(f"No PDFs found for grade {args.grade} in {args.data_dir}")
        return

    print(f"Found {len(pdf_files)} PDFs for grade {args.grade}")
    
    for pdf_path in pdf_files:
        filename = os.path.basename(pdf_path)
        subject = map_filename_to_subject(filename)
        print(f"\n--- Processing {filename} (Subject: {subject}) ---")
        
        extracted_json_path = os.path.join(temp_extract_dir, filename.replace('.pdf', '.json'))
        subject_out_dir = os.path.join(args.output_dir, f"grade{args.grade}_{subject}")
        
        # Step 1: Extract
        extract_cmd = [sys.executable, extract_script, pdf_path, extracted_json_path]
        print("Running:", " ".join(extract_cmd))
        if not args.dry_run:
            if not os.path.exists(extracted_json_path):
                subprocess.run(extract_cmd, check=True)
            else:
                print(f"Extraction for {filename} already exists, skipping...")
                
        # Step 2: Generate
        gen_cmd = [sys.executable, generate_script, extracted_json_path, subject_out_dir, "--grade", args.grade, "--subject", subject]
        print("Running:", " ".join(gen_cmd))
        if not args.dry_run:
            subprocess.run(gen_cmd, check=True)

    print("\nPipeline completed successfully!")

if __name__ == "__main__":
    main()

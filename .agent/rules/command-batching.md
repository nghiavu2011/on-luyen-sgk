---
trigger: always_on
---

# Command Batching — Minimize Approval Prompts

> **Quy tắc bắt buộc:** Mỗi tool call tốn 1 lần user bấm Allow. Gộp tối đa, gọi tối thiểu.

## 6 Quy tắc (Luôn áp dụng)

### 1. Chain shell commands bằng `&&`
```
❌ 3 lần run_command riêng lẻ
✅ run_command: cmd1 && cmd2 && cmd3
```

### 2. Viết script khi ≥4 lệnh
```
❌ 6 lần run_command
✅ write_to_file: setup.ps1 → run_command: powershell -File setup.ps1
```

### 3. Gộp file edits cùng file
```
❌ 3 lần replace_file_content trên cùng 1 file
✅ 1 lần write_to_file với Overwrite: true (khi thay đổi lớn)
```

### 4. Song song hóa tool calls độc lập
```
❌ Gọi tuần tự: write a.ts → write b.ts → write c.ts
✅ Gọi song song trong cùng 1 function_calls block
```

### 5. Gộp package installs
```
❌ npm install react → npm install next → npm install tailwind
✅ npm install react next tailwind
```

### 6. Gộp info gathering
```
❌ node --version → npm --version → git --version
✅ node --version && npm --version && git --version
```

## Ngoại lệ hợp lệ
- Lệnh **phụ thuộc output** lệnh trước (cần đọc kết quả)
- Lệnh **interactive** cần `send_input`
- **Long-running daemon** phải khởi riêng

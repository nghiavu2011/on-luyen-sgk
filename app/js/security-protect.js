/**
 * js/security-protect.js — Hệ thống Bảo Mật, An Toàn & Chống Sao Chép Toàn Diện
 * Bản quyền: N&Mstudio Education (www.nmstudio.id.vn)
 * Triết lý Ponytail: Thuần Native Web API, Zero External Dependencies, Siêu nhẹ (<3KB)
 */

(function() {
    'use strict';

    // 1. CHỐNG NHÚNG IFRAME TRÁI PHÉP (Clickjacking Defense)
    try {
        if (window.self !== window.top) {
            window.top.location = window.self.location;
        }
    } catch (e) {
        // Cross-origin iframe frame-busting
        try {
            document.body.style.display = 'none';
        } catch (err) {}
    }

    // 2. HỘP THÔNG BÁO BẢO VỆ BẢN QUYỀN (Toast Notification)
    let toastTimeout = null;
    function showSecurityToast(message) {
        let toast = document.getElementById('nm-security-toast');
        if (!toast) {
            toast = document.createElement('div');
            toast.id = 'nm-security-toast';
            toast.style.cssText = `
                position: fixed;
                bottom: 2rem;
                left: 50%;
                transform: translateX(-50%) translateY(100px);
                background: rgba(15, 23, 42, 0.94);
                color: #ffffff;
                padding: 0.85rem 1.35rem;
                border-radius: 30px;
                font-size: 0.88rem;
                font-weight: 600;
                box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3), 0 0 0 1px rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(10px);
                z-index: 999999;
                display: flex;
                align-items: center;
                gap: 0.6rem;
                transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.3s ease;
                opacity: 0;
                pointer-events: none;
                max-width: 90vw;
                text-align: center;
                border-left: 4px solid #0284c7;
            `;
            document.body.appendChild(toast);
        }

        toast.innerHTML = `<span>🛡️</span> <span id="nm-toast-msg"></span>`;
        const msgSpan = toast.querySelector('#nm-toast-msg');
        if (msgSpan) {
            msgSpan.textContent = message || 'Nội dung học tập được bảo hộ bản quyền bởi N&Mstudio Education!';
        }
        toast.style.transform = 'translateX(-50%) translateY(0)';
        toast.style.opacity = '1';

        if (toastTimeout) clearTimeout(toastTimeout);
        toastTimeout = setTimeout(() => {
            toast.style.transform = 'translateX(-50%) translateY(100px)';
            toast.style.opacity = '0';
        }, 2800);
    }

    // 3. VÔ HIỆU HÓA CHUỘT PHẢI (Context Menu Prevention)
    document.addEventListener('contextmenu', function(e) {
        // Cho phép chuột phải trong ô nhập liệu (input, textarea)
        const target = e.target;
        if (target && (target.tagName === 'INPUT' || target.tagName === 'TEXTAREA' || target.isContentEditable)) {
            return;
        }
        e.preventDefault();
        showSecurityToast('Tính năng chuột phải đã được khóa để bảo vệ bản quyền nội dung!');
    }, { capture: true });

    // 4. VÔ HIỆU HÓA PHÍM TẮT SAO CHÉP, IN ẤN & XEM NGUỒN (Keyboard Protection)
    document.addEventListener('keydown', function(e) {
        const target = e.target;
        const isInput = target && (target.tagName === 'INPUT' || target.tagName === 'TEXTAREA' || target.isContentEditable);
        
        // Cho phép sao chép/dán bình thường TRONG ô nhập liệu
        if (isInput && !e.ctrlKey && !e.metaKey) {
            return;
        }

        const key = e.key ? e.key.toLowerCase() : '';
        const keyCode = e.keyCode || e.which;
        const ctrlOrMeta = e.ctrlKey || e.metaKey;

        // F12 (DevTools)
        if (keyCode === 123 || key === 'f12') {
            e.preventDefault();
            e.stopPropagation();
            showSecurityToast('Tính năng kiểm tra mã nguồn đã bị vô hiệu hóa.');
            return false;
        }

        // Các tổ hợp Ctrl/Cmd + Key
        if (ctrlOrMeta) {
            // Ctrl+C (Copy) ngoài ô input
            if ((key === 'c' || keyCode === 67) && !isInput) {
                e.preventDefault();
                e.stopPropagation();
                showSecurityToast('Nội dung đề thi và bài giảng được bảo vệ, vui lòng không sao chép!');
                return false;
            }

            // Ctrl+U (Xem mã nguồn)
            if (key === 'u' || keyCode === 85) {
                e.preventDefault();
                e.stopPropagation();
                showSecurityToast('Xem mã nguồn đã bị khóa.');
                return false;
            }

            // Ctrl+S (Lưu trang)
            if (key === 's' || keyCode === 83) {
                // Ngoại trừ phím tắt 'S' đọc flashcard khi không bấm Ctrl
                e.preventDefault();
                e.stopPropagation();
                showSecurityToast('Lưu trang ngoại tuyến đã bị vô hiệu hóa.');
                return false;
            }

            // Ctrl+P (In ấn trang / Xuất PDF trộm đề)
            if (key === 'p' || keyCode === 80) {
                e.preventDefault();
                e.stopPropagation();
                showSecurityToast('In ấn và xuất PDF đã được khóa để bảo mật đề thi.');
                return false;
            }

            // Ctrl+Shift+I, Ctrl+Shift+J, Ctrl+Shift+C (DevTools / Inspect)
            if (e.shiftKey && (key === 'i' || key === 'j' || key === 'c' || keyCode === 73 || keyCode === 74 || keyCode === 67)) {
                e.preventDefault();
                e.stopPropagation();
                showSecurityToast('Công cụ phát triển (DevTools) đã bị vô hiệu hóa.');
                return false;
            }
        }
    }, { capture: true });

    // 5. CHỐNG BÔI ĐEN & SAO CHÉP QUA CLIPBOARD (Clipboard Protection)
    document.addEventListener('copy', function(e) {
        const target = e.target;
        if (target && (target.tagName === 'INPUT' || target.tagName === 'TEXTAREA')) {
            return; // Cho phép copy trong ô input cá nhân
        }
        e.preventDefault();
        if (e.clipboardData) {
            e.clipboardData.setData('text/plain', 'Nội dung học tập được bảo hộ độc quyền bởi N&Mstudio Education (https://onluyen-sgk.vercel.app). Mọi hành vi sao chép không xin phép đều bị nghiêm cấm.');
        }
        showSecurityToast('Nội dung câu hỏi và tài liệu đã được bảo vệ bản quyền!');
    });

    document.addEventListener('cut', function(e) {
        const target = e.target;
        if (target && (target.tagName === 'INPUT' || target.tagName === 'TEXTAREA')) {
            return;
        }
        e.preventDefault();
    });

    // 6. CHỐNG KÉO THẢ NỘI DUNG & HÌNH ẢNH (Drag-and-Drop Prevention)
    document.addEventListener('dragstart', function(e) {
        const target = e.target;
        if (target && target.tagName === 'IMG') {
            e.preventDefault();
        }
    });

    // 7. CẢNH BÁO BẢN QUYỀN TRÊN CONSOLE LOG (Console Defense)
    try {
        console.clear();
        console.log(
            '%c🛑 CẢNH BÁO BẢO MẬT & BẢN QUYỀN %c\n' +
            'Hệ thống Ôn Luyện SGK thuộc bản quyền của N&Mstudio Education.\n' +
            'Mọi hành vi trích xuất, sao chép hoặc phân phối lại nội dung câu hỏi/bài giảng đều vi phạm quyền sở hữu trí tuệ.',
            'background: #dc2626; color: white; font-weight: 800; font-size: 16px; padding: 6px 12px; border-radius: 6px;',
            'color: #334155; font-size: 12px; line-height: 1.6; font-weight: 500;'
        );
    } catch (e) {}

    window.showSecurityToast = showSecurityToast;
})();

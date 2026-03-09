// Template Switcher
(function() {
    const templateButtons = document.querySelectorAll('.template-btn');
    const currentTemplate = '{{CURRENT_TEMPLATE}}';
    
    templateButtons.forEach(btn => {
        btn.addEventListener('click', function() {
            const template = this.dataset.template;
            if (template === currentTemplate) return;
            
            // 現在のURLを解析
            const currentPath = window.location.pathname;
            const fileName = currentPath.split('/').pop();
            
            // 新しいファイル名を生成
            const newFileName = `${template}_output.html`;
            const newPath = currentPath.replace(fileName, newFileName);
            
            // 新しいテンプレートファイルが存在するか確認して遷移
            // Note: 実際の実装では、すべてのテンプレートで事前生成しておくか、
            // サーバーサイドで動的に生成する必要があります
            window.location.href = newPath;
        });
    });
})();
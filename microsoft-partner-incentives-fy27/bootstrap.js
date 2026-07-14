(async function(){
  const host=document.getElementById('app');
  const base='https://raw.githubusercontent.com/jianzhinanhai/AI-Study-PPT/main/microsoft-partner-incentives-fy27/';
  const loadText=async file=>{
    const response=await fetch(base+file,{cache:'no-cache'});
    if(!response.ok) throw new Error(`Failed to load ${file}: ${response.status}`);
    return response.text();
  };
  try{
    const cssFiles=['styles-1.css','styles-2.css','styles-3.css','styles-4.css'];
    const cssTexts=await Promise.all(cssFiles.map(loadText));
    cssTexts.forEach((css,index)=>{
      const style=document.createElement('style');
      style.dataset.source=cssFiles[index];
      style.textContent=css;
      document.head.appendChild(style);
    });

    const htmlFiles=['content-1.html','content-2.html','content-3.html'];
    const htmlParts=await Promise.all(htmlFiles.map(loadText));
    host.className='';
    host.innerHTML=htmlParts.join('');

    for(const file of ['decision-data.js','rate-data.js','app.js']){
      const code=await loadText(file);
      const script=document.createElement('script');
      script.dataset.source=file;
      script.textContent=code;
      document.body.appendChild(script);
    }
  }catch(error){
    console.error(error);
    host.className='';
    host.innerHTML='<main class="load-error"><h1>页面加载失败</h1><p>请刷新页面；若问题持续，请检查 GitHub 网络连接。</p></main>';
  }
})();

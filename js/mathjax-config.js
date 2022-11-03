
window.MathJax = {
  chtml: {
    displayAlign: "center"
  },
  tex: {
    inlineMath: [ ['$','$'], ["\\(","\\)"] ],
    processEscapes: true,
    packages: ['base', 'ams', 'noerrors', 'noundefined']
  },
  options: {
    ignoreHtmlClass: 'tex2jax_ignore',
    processHtmlClass: 'tex2jax_process'
  },
  loader: {
    load: ['[tex]/noerrors']
  }
}

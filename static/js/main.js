var copyTextareaBtn = document.querySelector('#copyBtn');

copyTextareaBtn.addEventListener('click', function(event) {
  var copyTextarea = document.querySelector('#dlLink');
  copyTextarea.focus();
  copyTextarea.select();

  try {
    var successful = document.execCommand('copy');
    document.querySelector("#isCopied").innerHTML = "Succesfully copied the link to your clipboard!";
  } catch (err) {
    console.log('Oops, unable to copy');
  }
});
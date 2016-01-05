$(document).ready(function()	{
    // alert('1');
   // $('.markitup').markItUp(myMarkdownSettings);


    $('#name').blur(function(){
       // alert(this.value);
        var pinyins=pinyin.getFullChars(this.value);
        $('#slug').val(pinyins);
    })




    });
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8">
	<title>Image Editor | Home</title>
    <link href="<?= base_url("assets/fotorama/fotorama.css") ?>" rel="stylesheet">
	<style>
    .fotorama__wrap{
        display: block;
        margin: 0px auto;

    }
    .download {
      /*width:20px;*/
      font-size: 29px;
      color: #eee;
    }
    .download:hover {
      color: #ee0000;
    }
    .download_div {
      position: fixed;
      top:10px;
      left: 10px;
      opacity: .0 ;
    }
    .download_div:hover {
      opacity: .9 !important;
      
    }
    /*.fotorama__stage{
        max-height: 600px !important
    }*/
    /*.fotorama__img{
      height: 100% !important;
    }*/
	</style>
      <!-- Fotorama -->
  
  <script src="<?= base_url("assets/jquery.js") ?>"></script>
  <script src="<?= base_url("assets/fotorama/fotorama.js") ?>"></script>

	<link rel="stylesheet" href="<?= base_url("assets/css/bootstrap.min.css") ?>">
</head>

<body style="background: #313B3B">
<div class="fotorama"
     data-nav="thumbs"
     data-height="100%"
     >
     <a href="<?= base_url('files/'.$dir.'/'.$file) ?>"><img src="<?= base_url('files/'.$dir.'/thumbnail/'.$file) ?>" /></a>
<?php for($i=1; $i<26; $i++):?>
    <a href="<?= site_url('home/get_filtered_image/'.$dir.'/'.$i.'/'.$file) ?>"><img src="<?= base_url('files/'.$dir.'/thumbnail/'.$i.'_'.$file) ?>" /></a>
    <?php endfor;?>
    
</div>
<div id="download" class="download_div">

  <a id="download_link" download>
  <span class="glyphicon glyphicon-download-alt download" ></span>
  </a>
</div>
<script>
$(document).ready(function(){
  var vi = false;
  var ioo;
  $(document).on('click', '#download_link', function() {

    ioo = $('.fotorama__nav__shaft').find('.fotorama__active').find('.fotorama__img').attr('src');

    var i = ioo.indexOf('thumbnail/');
    
    var l1 = ioo.substr(0, i);
    var l2 = ioo.substr(i+9);

    var link = l1+l2;
    console.log(ioo + " -- " + i + "  ==  "+l2);
    $('#download_link').attr('href', link);
  });

  window.onresize=function(){
    var img = $('.fotorama__stage__frame').find('.fotorama__img').offset();
        // ioo = $('.fotorama__img').attr('src');
        
          $('.download_div').css({
          top: (parseInt(img.top) + 10),
          left: (parseInt(img.left) + 10)
        });
        
        
  };

  $(document).on('click', '.fotorama__grab', function() {

    // ioo = $(this).find('.fotorama__active').find('.fotorama__img').attr('src');
    // // console.log($(this).find('.fotorama__active') +"  " +$(this).find('.fotorama__active').find('.fotorama__img').attr('src')+ "  " + $(this));
    // var i = ioo.indexOf('thumbnail/');
    
    // var l1 = ioo.substr(0, i);
    // var l2 = ioo.substr(i+9);

    // var link = l1+l2;

    // $('#download_link').attr('href', link);
    
    // window.location.assign(img+"/download");
  });

    $(document).on('mouseenter','.fotorama__stage__frame',function(){
        // $(this).attr('value',$(this).val());
        // console.log("jvhhj");
        var img = $('.fotorama__stage__frame').find('.fotorama__img').offset();
        // ioo = $('.fotorama__img').attr('src');
        if(!vi) {
          $('.download_div').css({
          top: (parseInt(img.top) + 10),
          left: (parseInt(img.left) + 10)
        });
        vi = true;
        }

        $('.download_div').css({
          
          opacity: 0.9
        });
    });
    $(document).on('mouseleave','.fotorama__stage__frame',function(){
        // $(this).attr('value',$(this).val());
        // console.log("jvhhj");
          // $('#download').hide();
          $('.download_div').css({
          opacity: 0
        });
    });
});
</script>
</body> 
</html>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Image Editor | Home</title>
    <style>
    .fileUpload {
    position: relative;
    overflow: hidden;
    margin: 10px;
    display: inline-block;
    padding: 50px 50px 50px 50px;
}
.fileUpload input.upload {
    position: absolute;
    top: 0;
    right: 0;
    margin: 0;
    padding: 0;
    font-size: 20px;
    cursor: pointer;
    opacity: 0;
    filter: alpha(opacity=0);
}
.main_div{
    text-align: center;
    
}
.title {
    font-family: serif;
    color: #ccc;
    font-size: 10em;
}
.name {
    font-family: cursive;
    color: #ccc;
    font-size: 2em;
}
.upload_text {
    font-family: sans-serif;
    font-size: 20px;
    color: #ccc;
}
.upload_button_text {
    font-family: sans-serif;
    font-size: 20px;
}
.base{
    background: #192A45;
}
.bar {
    height: 10px;
    background: #627BA3;
}
#progress {
    background: #ccc;
    width: 30%;
    height: 10px;
    display: inline-block;
}
    </style>
    <link rel="stylesheet" href="<?= base_url("assets/css/bootstrap.min.css") ?>">
</head>

<body class="base">
    <div class="main_div">
        <p class="title">Image Editor</p>
        <p class="name">by Abhishek Banerjee</p>
        <p class="upload_text">Upload Your Image</p>
        <div class="fileUpload btn btn-primary">
            <span class="upload_button_text">Upload</span>
            <input id="fileupload" class="upload" type="file" name="files[]" data-url="<?= site_url("home/upload_base_image"); ?>">
        </div>
        <br><br>
        <div id="progress">
    <div class="bar" style="width: 0%;"></div>
</div>
    </div>

<script src="<?= base_url("assets/jquery.js") ?>"></script>
<script src="<?= base_url("assets/jQueryFileUpload/js/vendor/jquery.ui.widget.js") ?>"></script>
<script src="<?= base_url("assets/jQueryFileUpload/js/jquery.iframe-transport.js") ?>"></script>
<script src="<?= base_url("assets/jQueryFileUpload/js/jquery.fileupload.js") ?>"></script>
<script>
$(function () {
    var pr;
    var progress = 0;
    var r = Math.random()*30+30;
    $('#fileupload').fileupload({
        dataType: 'json',
        add: function (e, data) {
            var jqXHR = data.submit()
            .success(function (result, textStatus, jqXHR) {
                console.log("bkj");
            })
            .error(function (jqXHR, textStatus, errorThrown) {

            })
            .complete(function (result, textStatus, jqXHR) {
                console.log("bkj");
            });
        pr = setInterval(function(){ 
            progress += 1;
        
            if(progress < r) {
                progress += 1;
            }
            else {
                clearInterval(pr);
            }
            $('#progress .bar').css(
            'width',
            progress + '%'
        );
         }, 40);
        },
        progressall: function (e, data) {
        // var progress = parseInt(data.loaded / data.total * 100, 10);
        // $('#progress .bar').css(
        //     'width',
        //     progress-30 + '%'
        // );
    },
        done: function (e, data) {
            pr = setInterval(function(){ 
            progress += 1;
        
            if(progress < 100) {
                progress += 1;
                $('#progress .bar').css(
            'width',
            progress + '%'
        );
            }
            else {
                clearInterval(pr);
                $.each(data.result.files, function (index, file) {
                
                console.log(file);
                // window.location.assign("<?= base_url('editor/')?>/"+file.name);
                window.location.assign("<?= site_url('home/edit_view')?>/"+data.result.directory+'/'+file.name);
            });
            }
            $('#progress .bar').css(
            'width',
            progress + '%'
        );
         }, 40);
            
        }
    });
});
</script>
</body> 
</html>
<!-- 
<body>
<script src="<?= base_url("assets/jquery.js") ?>"></script>
<script src="<?= base_url("assets/jQueryFileUpload/js/vendor/jquery.ui.widget.js") ?>"></script>
<script src="<?= base_url("assets/jQueryFileUpload/js/jquery.iframe-transport.js") ?>"></script>
<script src="<?= base_url("assets/jQueryFileUpload/js/jquery.fileupload.js") ?>"></script>
<script>
$(function () {
    $('#fileupload').fileupload({
        dataType: 'json',
        done: function (e, data) {
            console.log(data);
            $.each(data.result.files, function (index, file) {
            	console.log(data.result.directory);
            	window.location.assign("<?= site_url('home/edit_view')?>/"+data.result.directory+'/'+file.name);
                
            });
        }
    });
});
</script>
</body> 
</html> -->
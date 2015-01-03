<?php if ( ! defined('BASEPATH')) exit('No direct script access allowed');

class Home extends CI_Controller {

	/**
	 * Index Page for this controller.
	 *
	 * Maps to the following URL
	 * 		http://example.com/index.php/welcome
	 *	- or -  
	 * 		http://example.com/index.php/welcome/index
	 *	- or -
	 * Since this controller is set as the default controller in 
	 * config/routes.php, it's displayed at http://example.com/
	 *
	 * So any other public methods not prefixed with an underscore will
	 * map to /index.php/welcome/<method_name>
	 * @see http://codeigniter.com/user_guide/general/urls.html
	 */
	public function index()
	{
		$this->load->view('home_view');
	}
	
	public function upload_base_image() {
		
		$GLOBALS['directory'] = $this->generateRandomString(10);
		require('UploadHandler.php');
		$upload_handler = new UploadHandler();
		// echo "python ".FCPATH."assets/script/editor.py ".$GLOBALS['im_name']." ".$GLOBALS['directory']." 0";
		exec("python ".FCPATH."assets/script/editor.py ".$GLOBALS['im_name']." ".$GLOBALS['directory']." 0");
	}

	public function edit_view($d="", $f="") {
		$this->load->view('edit', array('dir'=>$d, 'file'=>$f));
	}
	
	public function h() {
		// echo exec("python ".FCPATH."/assets/script/editor.py in.jpg f 0");
		exec("python ".FCPATH."/assets/script/editor.py in.jpg f 0");
		// $command = escapeshellcmd('python /home/abhishek/Documents/php/codeigniter/imageEditor/assets/script/editor.py in.jpg f 0');
		// $output = shell_exec($command);
		// echo $output;
	}

	public function get_filtered_image($d, $i, $im_name, $down = "view")
	{
		// if($down == 'view') {
			$type = substr($im_name, strpos($im_name, '.')+1);
			// echo "$type";
			if(!file_exists(FCPATH.'files/'.$d.'/'.$i.'_'.$im_name)) {
				exec("python ".FCPATH."assets/script/editor.py ".$im_name." ".$d." ".$i);
			}
			$name = FCPATH.'files/'.$d.'/'.$i.'_'.$im_name;
			$fp = fopen($name, 'r');

			// send the right headers
			header("Content-Type: image/".$type);
			header("Content-Length: " . filesize($name));

			// dump the picture and stop the script
			fpassthru($fp);
			// exit;
		// }
	}

	public function g() {
		$str = "2at5zqt7jtazgviq7wj9.jpeg";
        // echo 'python '.FCPATH
        //     .'assets/script/editor.py '.$str.' '.'og8FVSMsgH'.' 0';
        // echo exec('python editor.py '.$str.' '.$GLOBALS['directory'].' 0');
        // $command = escapeshellcmd('python '.FCPATH
        //     .'assets/script/editor.py '.$str.' '.'og8FVSMsgH'.' 0');
        $pyscript = 'C:\Users\Abhishek\Downloads\Compressed\xampp\htdocs\imageEditor\assets\script\editor.py in.jpg f 0';
$python = 'C:\Python27\python.exe';

$cmd = "$pyscript";
echo $cmd;
		echo exec($cmd);
		// $command = 'C:\Python27\python.exe '.FCPATH
  //           .'assets\script\ttpy.py';
  //       echo ''.$command;
  //       $output = exec($command);
        // echo $output;
        // die();
	}
	
	public function generateRandomString($length = 10) {
    $characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    $charactersLength = strlen($characters);
    $randomString = '';
    for ($i = 0; $i < $length; $i++) {
        $randomString .= $characters[rand(0, $charactersLength - 1)];
    }
    return $randomString;
}
}

/* End of file welcome.php */
/* Location: ./application/controllers/welcome.php */
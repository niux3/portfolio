<?php
    namespace src\core\libs\captcha;

    use src\core\libs\captcha\chars\AnsiShadow;
    use src\core\libs\captcha\chars\Big;
    use src\core\libs\captcha\chars\Standard;
    

    class AsciiCaptcha {

        private $noiseChars = array( ' ', "=", "-", ":", "!", "~", "[", '(', "{", "|", "^", "}", "]", ")", "`", ",", " ");
        private $asciiFonts = array();
        public $countChars = 4;
        const salt = 'Pyth0n!$B€tt€|2';


        public function __construct($cls_name=null){
            $path_chars = 'chars';
            if(is_null($cls_name)){
                $files = array_values(array_filter(scandir($path_chars), function($i){ return $i !== "." && $i !== ".."; }));
                $cls_name = str_replace('.php', '', $files[array_rand($files)]);
            }

            require_once sprintf('%s/%s.php', $path_chars, $cls_name);
            $cls = sprintf('\src\core\libs\captcha\chars\%s', $cls_name);
            $this->asciiFonts = $cls::get();
        }

        public static function getSalt(){
            return AsciiCaptcha::salt;
        }

        public function getCaptcha() {
    	    $chars = array();
    	    $captchaChars = array_rand( $this->asciiFonts, $this->countChars );
    	    for ($idx = 0; $idx < sizeof( $captchaChars ); $idx++) {
    	       $capChar = $captchaChars[$idx];
    	       $chars[ $capChar ] = $this->asciiFonts[ $capChar ];
    	    }

    	    $chars = $this->addNoise( $chars );
            $result = [
                'token' => hash('sha256', implode('', array_keys($chars)).AsciiCaptcha::salt),
                'captcha' => $chars
            ];
    	    return $result;
    	}

    	private function addNoise( $captchaStrings ) {
    	    $result = array();
    	    foreach( $captchaStrings as $capChar => $ascii ) {
        		for ($idx = 0; $idx < strlen( $ascii ); $idx++) {
        		    if ( $ascii[$idx] == ' ' ) {
            			$noiseChar = array_rand( $this->noiseChars, 1 );
            			$ascii[$idx] = $this->noiseChars[$noiseChar];
        		    }
        		}

        		$ascii = str_replace ( chr(13), '  ', $ascii );
        		$result[ $capChar ] = $ascii;
    	    }

    	    return $result;
    	}
    }

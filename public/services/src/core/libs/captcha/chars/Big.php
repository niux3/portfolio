<?php
    namespace src\core\libs\captcha\chars;


    class Big{
        public static function get(){
            $fonts["A"] = "
            
    /\
   /  \
  / /\ \
 / ____ \
/_/    \_\\";
            $fonts["B"] = 
"____
|  _ \
| |_) |
|  _ <
| |_) |
|____/ ";
            $fonts["C"] =
" _____
 / ____|
| |
| |
| |____
 \_____|";
            $fonts["D"] = 
"_____
|  __ \
| |  | |
| |  | |
| |__| |
|_____/ ";
	    $fonts["E"] =
"______
|  ____|
| |__
|  __|
| |____
|______|";
            $fonts["F"] =
"______
|  ____|
| |__
|  __|
| |
|_|     ";
            $fonts["G"] =
" _____ 
 / ____|
| |  __ 
| | |_ |
| |__| |
 \_____|";
            $fonts["H"] =
" _    _ 
 | |  | |
 | |__| |
 |  __  |
 | |  | |
 |_|  |_|";
            $fonts["I"] =
" _____ 
 |_   _|
   | |  
   | |  
  _| |_ 
 |_____|";
            $fonts["J"] =
"      _ 
      | |
      | |
  _   | |
 | |__| |
  \____/ ";
            $fonts["K"] =
" _  __
 | |/ /
 | ' / 
 |  <  
 | . \ 
 |_|\_\\";
            $fonts["L"] =
" _      
 | |     
 | |     
 | |     
 | |____ 
 |______|";
            $fonts["M"] =
" __  __ 
 |  \/  |
 | \  / |
 | |\/| |
 | |  | |
 |_|  |_|";
            $fonts["N"] =
" _   _ 
 | \ | |
 |  \| |
 | . ` |
 | |\  |
 |_| \_|";
            $fonts["O"] = 
'  ____  
  / __ \ 
 | |  | |
 | |  | |
 | |__| |
  \____/ ';
            $fonts["P"] =
" _____  
 |  __ \ 
 | |__) |
 |  ___/ 
 | |     
 |_|     ";
            $fonts["Q"] =
"  ____  
  / __ \ 
 | |  | |
 | |  | |
 | |__| |
  \___\_\\";
            $fonts["R"] =
" _____  
 |  __ \ 
 | |__) |
 |  _  / 
 | | \ \ 
 |_|  \_\\";
            $fonts["S"] =
"  _____ 
  / ____|
 | (___  
  \___ \ 
  ____) |
 |_____/ ";
            $fonts["T"] =
" _______ 
 |__   __|
    | |   
    | |   
    | |   
    |_|   ";
            $fonts["U"] =
" _    _ 
 | |  | |
 | |  | |
 | |  | |
 | |__| |
  \____/ ";
            $fonts["V"] =
"__      __
 \ \    / /
  \ \  / / 
   \ \/ /  
    \  /   
     \/    ";
            $fonts["W"] =
"__          __
 \ \        / /
  \ \  /\  / / 
   \ \/  \/ /  
    \  /\  /   
     \/  \/    ";
            $fonts["X"] =
"__   __
 \ \ / /
  \ V / 
   > <  
  / . \ 
 /_/ \_\\";
            $fonts["Y"] =
"__     __
 \ \   / /
  \ \_/ / 
   \   /  
    | |   
    |_|  ";
            $fonts["Z"] =
" ______
 |___  /
    / / 
   / /  
  / /__ 
 /_____|";
            return $fonts;
        }
    }

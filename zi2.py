import time
from subprocess import call

i = 0;
while(i < 100):
    call(["clear"])
    print i * " ", "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
    print i * " ", "                        $$$"
    print i * " ", "                      $$$"
    print i * " ", "                    $$$"
    print i * " ", "                  $$$"
    print i * " ", "                $$$"
    print i * " ", "              $$$"
    print i * " ", "            $$$"
    print i * " ", "          $$$"
    print i * " ", "        $$$"
    print i * " ", "      $$$"
    print i * " ", "   $$$"
    print i * " ", " $$$"
    print i * " ", "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
    time.sleep(0.3)
    i = i + 1;

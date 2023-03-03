if(${?LD_LIBRARY_PATH}) then
    setenv LD_LIBRARY_PATH ${LD_LIBRARY_PATH}:.
    echo $LD_LIBRARY_PATH
else
    setenv LD_LIBRARY_PATH .
endif

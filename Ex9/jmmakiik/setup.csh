if(${?LD_LIBRARY_PATH}) then
    setenv LD_LIBRARY_PATH ${LD_LIBRARY_PATH}:.
    echo $LD_LIBRARY_PATH
else
    setenv LD_LIBRARY_PATH .
endif

if(${?PYTHONPATH}) then
    setenv PYTHONPATH ${PYTHONPATH}:.
    echo $PYTHONPATH
else
    setenv PYTHONPATH .
endif

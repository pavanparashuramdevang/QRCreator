import datetime
import os

def random_filename():
    directory='static/images'
    basename = "resultQr"
    extension=r'.png'
    path=os.getcwd()
    suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
    filename = "_".join([basename, suffix]) # e.g. 'mylogfile_120508_171442'
    using_name = "_".join([basename, suffix])
    filename='/'.join([directory,filename])
    filename=''.join([filename,extension])
    using_name=''.join([using_name,extension])
    using_name='images/'+str(using_name)
    filename='/'.join([path,filename])
    # filename=filename.replace('\\','\\\\')
    return str(filename),using_name



if __name__=="__main__":
    print(random_filename())
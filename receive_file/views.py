import datetime

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def upload_file(request):

    # 请求方法为POST时,进行处理;

    if request.method == "POST":

        # 获取上传的文件,如果没有文件,则默认为None;

        File = request.FILES.get("file", None)

        if File is None:

            return HttpResponse("no files for upload!")

        else:
            print(File.name)
            filename = File.name
            end_name = filename.split(".")[-1]
            first_name = filename.split('.')[0]
            current_timestamp = str(datetime.datetime.now().timestamp() * 1000)
            filename_new = first_name+'_'+current_timestamp+'.'+end_name
            # 打开特定的文件进行二进制的写操作;
            with open("receive_file/static/%s" % filename_new, 'wb+') as f:
                # 分块写入文件;
                for chunk in File.chunks():
                    f.write(chunk)
            return HttpResponse("upload over!")
    return HttpResponse("need POST method!")
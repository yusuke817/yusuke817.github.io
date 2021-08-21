# HttpResponseクラスのインポート 
from django.http import HttpResponse 
# hello()関数 
# render関数のインポート 
from django.shortcuts import render
# ビュー 
def hello(request): 
    # テンプレートに渡す辞書 
    context = {'message':'メッセージ'} 
    return render(request, 'iekari/message.html', context=context) 
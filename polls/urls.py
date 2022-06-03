from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    #path('<int:question_id>/', views.detail, name='detail'),
    path('specifics/<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

'''
path() 関数は4つの引数を受け取ります。引数のうち route と view の2つは必須で、kwargs、name の2つは省略可能です。ここで、これらの引数がどのようなものか見てみましょう。

path() 引数: route¶
route は URL パターンを含む文字列です。リクエストを処理するとき、Django は urlpatterns のはじめのパターンから開始し、リストを順に下に見ていきます。要求された URL を一致するものを見つけるまで各パターンと比較します。

パターンはGETやPOSTのパラメーター、そしてドメイン名を検索しません。例えば、 https://www.example.com/myapp/ へのリクエストにおいては、URLconfは myapp/ を見ます。 https://www.example.com/myapp/?page=3 へのリクエストにおいても、URLconfは myapp/ を見ます。

path() 引数: view¶
Django がマッチする正規表現を見つけると、 Django は指定されたビュー関数を呼び出します。その際は HttpRequest オブジェクトを第一引数に、そしてキーワード引数としてrouteから「キャプチャされた」値を呼び出します。この例はこの後すぐ出てきます。

path() 引数: kwargs¶
任意のキーワード引数を辞書として対象のビューに渡せます。この機能はチュートリアルでは使いません。

path() 引数: name¶
URL に名前付けをしておけば Django のどこからでも明確に参照でき、とくにテンプレートの中で有効です。この便利な機能のおかげで、プロジェクトのURLにグローバルな変更を加える場合にも1つのファイルを変更するだけで済むようになります。

'''
## DDD勉強用プロジェクト
DjangoのpollsアプリにDDD(オニオンアーキテクチャ)を採用して作成したものです

## ディレクトリ構造

```
.
├─ config/: プロジェクト設定
├─ domain/: ドメイン情報
│   ├─ entity/: エンティティ
│   ├─ repository/: リポジトリ(IF、抽象クラス)
│   └─ service/: ドメインサービス
├─ polls/: pollsアプリ
│   ├─ apps: DI実行
│   ├─ service: アプリケーションサービス
│   ├─ repository/: リポジトリ(実態)
│   └─ inject_config/: DI設定
└─ tests/: テスト
    ├─ polls: pollsアプリのテスト
    └─ test_setting/: テストツール・設定
        ├─ repository/: テスト用リポジトリ(実態)
        ├─ base: テスト用基本クラス（テスト用DI設定を再注入している）
        └─ inject_config/: テスト用DI設定
```

## 注意点・課題
- DDD勉強用なのでエラーハンドリング等は完璧でなはい
- ドメインサービスに割り当てる処理がなかったので空になっている
- オニオンアーキテクチャに従うのであればリポジトリ(実態)はinfrastructureディレクトリに配置するべきなので必要ならディレクトリ構造を変える
- ディレクトリ・ファイルの命名規則はベストプラクティスなどを調べて再考したほうがいい気がする
- ORマッパーを使えばDBアクセスが１回で済むところがエンティティへの変換などを挟むことで複数回アクセスしなければならない、DDDに忠実に従うことと無駄のない処理(パフォーマンス)の両立が難しい（トレードオフなのか？）
- レコード取得処理が増えていくと取得条件の数だけリポジトリのメソッドが増えていってしまう、ベストプラクティスが知りたい

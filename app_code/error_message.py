class ErrorMessage:
    # コマンドライン引数に誤り
    ERROR_ARGMENTS_ILLEGAL = "コマンドライン引数を正しく指定してください"
    # フォルダではない
    ERROR_NOT_FOLDER = "コマンドライン引数に指定できるのはフォルダのみです"
    # フォルダ内にファイルが存在しない
    ERROR_EMPTY_FOLDER = "フォルダが存在しないまたはフォルダ内にファイルが存在しません"
    # 新規フォルダが既に存在
    ERROR_ALREADY_EXIST_FOLDER_NAME = "指定したフォルダ名は既に存在しているため、別のフォルダ名を指定してください"
    # 例外エラー
    ERROR_EXCEPTION = "予期せぬエラーが発生しました"

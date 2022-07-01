# ------------------------------------------------------------
#   実行ファイル  :  exe.py
# ------------------------------------------------------------
import os
import sys
import glob
import shutil
import datetime
import app_code.error_message

error_mess = app_code.error_message.ErrorMessage
month = ['January', 'February', 'March', 'April', 'May', 'June',
         'July', 'August', 'September', 'October', 'November', 'December']  # 月名
args = sys.argv  # コマンドライン引数
current_dir_path = os.getcwd()  # カレントディレクトリ


def main():
    """
    実行
    """
    # バリデーション
    if (ValidateArgs() != None):
        print("ERROR: " + ValidateArgs())
        return

    files = glob.glob(args[1] + "\*")
    if (len(files) < 1):
        print("ERROR: " + error_mess.ERROR_EMPTY_FOLDER)
        return

    # 新規フォルダ作成
    os.makedirs(current_dir_path + "\\" + args[2])

    for file in files:
        months_and_years = GetMontshAndYears(file)

        # 年ごとのフォルダを作成
        years_folder = current_dir_path + "\\" + \
            args[2] + "\\" + str(months_and_years[0])
        os.makedirs(years_folder, exist_ok=True)

        # 月ごとのフォルダを作成
        get_month = month[months_and_years[1] - 1]
        months_folder = current_dir_path + "\\" + \
            args[2] + "\\" + str(months_and_years[0]) + "\\" + get_month
        os.makedirs(months_folder, exist_ok=True)

        # 作成したフォルダにファイルをコピー
        if ("." in file):
            shutil.copy(file, months_folder)
        else:
            shutil.copytree(file, months_folder + "\\" + file.split("\\")[-1])

    print("Successful: フォルダが作成されました")


def ValidateArgs():
    """
    コマンドライン引数に対するバリデーション

    Returns: <string>エラーメッセージ
    """
    # コマンドライン引数の個数チェック
    if (len(args) != 3):
        return error_mess.ERROR_ARGMENTS_ILLEGAL

    # ファイル名を取得
    folder_name = args[1].split("\\")[-1]
    if ("." in folder_name):
        return error_mess.ERROR_NOT_FOLDER

    # 新規作成するフォルダが既に存在するか
    if os.path.isdir(current_dir_path + "\\" + args[2]):
        return error_mess.ERROR_ALREADY_EXIST_FOLDER_NAME
    return None


def GetMontshAndYears(file):
    """
    ファイルの作成日時から作成年月を取得

    params:
        <array>fails -> 対象ファイル

    Returns: <array>作成年月
    """
    array = []
    os_name = os.name
    get_datetime = ""
    if os_name == "nt":
        get_datetime = datetime.datetime.fromtimestamp(
            os.path.getctime(file))
    elif os_name == "posix":
        get_datetime = datetime.datetime.fromtimestamp(
            os.stat(file).st_birthtime)
    else:
        print("ERROR: " + error_mess.ERROR_EXCEPTION)
        exit()

    array.extend([int(str(get_datetime).split("-")[0]),
                  int(str(get_datetime).split("-")[1])])
    return array


if __name__ == '__main__':
    main()

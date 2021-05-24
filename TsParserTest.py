

# coding:UTF-8

import bitstring
from aribstr import *

# トランスポートストリームID
tsid_list = {
    32736:'ＮＨＫ総合・東京',
    32737:'ＮＨＫ教育・東京',
    32738:'日本テレビ',
    32739:'ＴＢＳ',
    32740:'フジテレビジョン',
    32741:'テレビ朝日',
    32742:'テレビ東京',
    32744:'放送大学',
    32721:'ＮＨＫ教育・大阪',
    32722:'ＭＢＳ毎日放送',
    32723:'ＡＢＣテレビ',
    32724:'関西テレビ',
    32725:'読売テレビ',
    32705:'ＮＨＫ教育・名古屋',
    32706:'東海テレビ',
    32707:'ＣＢＣ',
    32708:'メ～テレ',
    32709:'中京テレビ',
    32690:'ＨＢＣ北海道放送',
    32691:'ＳＴＶ札幌テレビ',
    32692:'ＨＴＢ北海道テレビ',
    32693:'ＵＨＢ',
    32694:'ＴＶＨ',
    32674:'ＲＮＣ西日本テレビ',
    32675:'ＫＳＢ瀬戸内海放送',
    32676:'ＲＳＫテレビ',
    32677:'ＴＳＣテレビせとうち',
    32678:'ＯＨＫテレビ',
    32658:'山陰中央テレビ',
    32659:'ＢＳＳテレビ',
    32660:'日本海テレビ',
    32592:'ＮＨＫ総合・札幌',
    32593:'ＮＨＫ教育・札幌',
    32594:'ＨＢＣ札幌',
    32595:'ＳＴＶ札幌',
    32596:'ＨＴＢ札幌',
    32597:'ＵＨＢ札幌',
    32598:'ＴＶＨ札幌',
    32576:'ＮＨＫ総合・函館',
    32577:'ＮＨＫ教育・函館',
    32578:'ＨＢＣ函館',
    32579:'ＳＴＶ函館',
    32580:'ＨＴＢ函館',
    32581:'ＵＨＢ函館',
    32582:'ＴＶＨ函館',
    32560:'ＮＨＫ総合・旭川',
    32561:'ＮＨＫ教育・旭川',
    32562:'ＨＢＣ旭川',
    32563:'ＳＴＶ旭川',
    32564:'ＨＴＢ旭川',
    32565:'ＵＨＢ旭川',
    32566:'ＴＶＨ旭川',
    32544:'ＮＨＫ総合・帯広',
    32545:'ＮＨＫ教育・帯広',
    32546:'ＨＢＣ帯広',
    32547:'ＳＴＶ帯広',
    32548:'ＨＴＢ帯広',
    32549:'ＵＨＢ帯広',
    32550:'ＴＶＨ帯広',
    32528:'ＮＨＫ総合・釧路',
    32529:'ＮＨＫ教育・釧路',
    32530:'ＨＢＣ釧路',
    32531:'ＳＴＶ釧路',
    32532:'ＨＴＢ釧路',
    32533:'ＵＨＢ釧路',
    32534:'ＴＶＨ釧路',
    32512:'ＮＨＫ総合・北見',
    32513:'ＮＨＫ教育・北見',
    32514:'ＨＢＣ北見',
    32515:'ＳＴＶ北見',
    32516:'ＨＴＢ北見',
    32517:'ＵＨＢ北見',
    32518:'ＴＶＨ北見',
    32496:'ＮＨＫ総合・室蘭',
    32497:'ＮＨＫ教育・室蘭',
    32498:'ＨＢＣ室蘭',
    32499:'ＳＴＶ室蘭',
    32500:'ＨＴＢ室蘭',
    32501:'ＵＨＢ室蘭',
    32502:'ＴＶＨ室蘭',
    32480:'ＮＨＫ総合・仙台',
    32481:'ＮＨＫ教育・仙台',
    32482:'ＴＢＣテレビ',
    32483:'仙台放送',
    32484:'ミヤギテレビ',
    32485:'ＫＨＢ東日本放送',
    32464:'ＮＨＫ総合・秋田',
    32465:'ＮＨＫ教育・秋田',
    32466:'ＡＢＳ秋田放送',
    32467:'ＡＫＴ秋田テレビ',
    32468:'ＡＡＢ秋田朝日放送',
    32448:'ＮＨＫ総合・山形',
    32449:'ＮＨＫ教育・山形',
    32450:'ＹＢＣ山形放送',
    32451:'ＹＴＳ山形テレビ',
    32452:'テレビユー山形',
    32453:'さくらんぼテレビ',
    32432:'ＮＨＫ総合・盛岡',
    32433:'ＮＨＫ教育・盛岡',
    32434:'ＩＢＣテレビ',
    32435:'テレビ岩手',
    32436:'めんこいテレビ',
    32437:'岩手朝日テレビ',
    32416:'ＮＨＫ総合・福島',
    32417:'ＮＨＫ教育・福島',
    32418:'福島テレビ',
    32419:'福島中央テレビ',
    32420:'ＫＦＢ福島放送',
    32421:'テレビユー福島',
    32400:'ＮＨＫ総合・青森',
    32401:'ＮＨＫ教育・青森',
    32402:'ＲＡＢ青森放送',
    32403:'ＡＴＶ青森テレビ',
    32404:'青森朝日放送',
    32391:'ＴＯＫＹＯ ＭＸ',
    32375:'ｔｖｋ',
    32359:'群馬テレビ',
    32336:'ＮＨＫ総合・水戸',
    32327:'チバテレビ',
    32311:'とちぎテレビ',
    32295:'テレ玉',
    32272:'ＮＨＫ総合・長野',
    32273:'ＮＨＫ教育・長野',
    32274:'テレビ信州',
    32275:'ａｂｎ長野朝日放送',
    32276:'ＳＢＣ信越放送',
    32277:'ＮＢＳ長野放送',
    32256:'ＮＨＫ総合・新潟',
    32257:'ＮＨＫ教育・新潟',
    32258:'ＢＳＮ',
    32259:'ＮＳＴ',
    32260:'ＴｅＮＹテレビ新潟',
    32261:'新潟テレビ２１',
    32240:'ＮＨＫ総合・甲府',
    32241:'ＮＨＫ教育・甲府',
    32242:'ＹＢＳ山梨放送',
    32243:'ＵＴＹ',
    32224:'ＮＨＫ総合・名古屋',
    32230:'テレビ愛知',
    32208:'ＮＨＫ総合・金沢',
    32209:'ＮＨＫ教育・金沢',
    32210:'テレビ金沢',
    32211:'北陸朝日放送',
    32212:'ＭＲＯ',
    32213:'石川テレビ',
    32192:'ＮＨＫ総合・静岡',
    32193:'ＮＨＫ教育・静岡',
    32194:'ＳＢＳ',
    32195:'テレビ静岡',
    32196:'だいいちテレビ',
    32197:'静岡朝日テレビ',
    32176:'ＮＨＫ総合・福井',
    32177:'ＮＨＫ教育・福井',
    32178:'ＦＢＣテレビ',
    32179:'福井テレビ',
    32160:'ＮＨＫ総合・富山',
    32161:'ＮＨＫ教育・富山',
    32162:'ＫＮＢ北日本放送',
    32163:'ＢＢＴ富山テレビ',
    32164:'チューリップテレビ',
    32144:'ＮＨＫ総合・津',
    32150:'三重テレビ',
    32128:'ＮＨＫ総合・岐阜',
    32134:'ぎふチャン',
    32112:'ＮＨＫ総合・大阪',
    32118:'テレビ大阪',
    32096:'ＮＨＫ総合・京都',
    32102:'ＫＢＳ京都',
    32080:'ＮＨＫ総合・神戸',
    32086:'サンテレビ',
    32064:'ＮＨＫ総合・和歌山',
    32070:'テレビ和歌山',
    32048:'ＮＨＫ総合・奈良',
    32054:'奈良テレビ',
    32032:'ＮＨＫ総合・大津',
    32038:'ＢＢＣびわ湖放送',
    32016:'ＮＨＫ総合・広島',
    32017:'ＮＨＫ教育・広島',
    32018:'ＲＣＣテレビ',
    32019:'広島テレビ',
    32020:'広島ホームテレビ',
    32021:'ＴＳＳ',
    32000:'ＮＨＫ総合・岡山',
    32001:'ＮＨＫ教育・岡山',
    31984:'ＮＨＫ総合・松江',
    31985:'ＮＨＫ教育・松江',
    31968:'ＮＨＫ総合・鳥取',
    31969:'ＮＨＫ教育・鳥取',
    31952:'ＮＨＫ総合・山口',
    31953:'ＮＨＫ教育・山口',
    31954:'ＫＲＹ山口放送',
    31955:'ｔｙｓテレビ山口',
    31956:'ｙａｂ山口朝日',
    31936:'ＮＨＫ総合・松山',
    31937:'ＮＨＫ教育・松山',
    31938:'南海放送',
    31939:'愛媛朝日',
    31940:'あいテレビ',
    31941:'テレビ愛媛',
    31920:'ＮＨＫ総合・高松',
    31921:'ＮＨＫ教育・高松',
    31904:'ＮＨＫ総合・徳島',
    31905:'ＮＨＫ教育・徳島',
    31906:'四国放送',
    31888:'ＮＨＫ総合・高知',
    31889:'ＮＨＫ教育・高知',
    31890:'高知放送',
    31891:'テレビ高知',
    31892:'さんさんテレビ',
    31872:'ＮＨＫ総合・福岡',
    30848:'ＮＨＫ総合・北九州',
    31873:'ＮＨＫ教育・福岡',
    30849:'ＮＨＫ教育・北九州',
    31874:'ＫＢＣ九州朝日放送',
    31875:'ＲＫＢ毎日放送',
    31876:'ＦＢＳ福岡放送',
    31877:'ＴＶＱ九州放送',
    31878:'ＴＮＣテレビ西日本',
    31856:'ＮＨＫ総合・熊本',
    31857:'ＮＨＫ教育・熊本',
    31858:'ＲＫＫ熊本放送',
    31859:'ＴＫＵテレビ熊本',
    31860:'ＫＫＴくまもと県民',
    31861:'ＫＡＢ熊本朝日放送',
    31840:'ＮＨＫ総合・長崎',
    31841:'ＮＨＫ教育・長崎',
    31842:'ＮＢＣ長崎放送',
    31843:'ＫＴＮテレビ長崎',
    31844:'ＮＣＣ長崎文化放送',
    31845:'ＮＩＢ長崎国際テレビ',
    31824:'ＮＨＫ総合・鹿児島',
    31825:'ＮＨＫ教育・鹿児島',
    31826:'ＭＢＣ南日本放送',
    31827:'ＫＴＳ鹿児島テレビ',
    31828:'ＫＫＢ鹿児島放送',
    31829:'ＫＹＴ鹿児島読売ＴＶ',
    31808:'ＮＨＫ総合・宮崎',
    31809:'ＮＨＫ教育・宮崎',
    31810:'ＭＲＴ宮崎放送',
    31811:'ＵＭＫテレビ宮崎',
    31792:'ＮＨＫ総合・大分',
    31793:'ＮＨＫ教育・大分',
    31794:'ＯＢＳ大分放送',
    31795:'ＴＯＳテレビ大分',
    31796:'ＯＡＢ大分朝日放送',
    31776:'ＮＨＫ総合・佐賀',
    31777:'ＮＨＫ教育・佐賀',
    31778:'ＳＴＳサガテレビ',
    31760:'ＮＨＫ総合・那覇',
    31761:'ＮＨＫ教育・那覇',
    31762:'ＲＢＣテレビ',
    31764:'ＱＡＢ琉球朝日放送',
    31767:'沖縄テレビ (ＯＴＶ)',
}

# サービスID
sid_list = {
    1024:'ＮＨＫ総合１・東京',
    1025:'ＮＨＫ総合２・東京',
    1408:'ＮＨＫ携帯Ｇ・東京',
    1032:'ＮＨＫＥテレ１東京',
    1033:'ＮＨＫＥテレ１東京',
    1034:'ＮＨＫＥテレ１東京',
    1416:'ＮＨＫ携帯２',
    24632:'ｔｖｋ１',
    25016:'ｔｖｋ',
    1040:'日テレ１',
    1041:'日テレ２',
    1424:'日本テレビ',
    1064:'テレビ朝日',
    1065:'テレビ朝日',
    1066:'テレビ朝日',
    1448:'テレビ朝日',
    1048:'ＴＢＳ１',
    1049:'ＴＢＳ２',
    1432:'ＴＢＳ',
    1183:'Ｇガイド',
    1072:'テレビ東京１',
    1073:'テレビ東京２',
    1074:'テレビ東京３',
    1456:'テレビ東京携帯',
    1056:'フジテレビ',
    1057:'フジテレビ',
    1058:'フジテレビ',
    1440:'フジテレビ',
    23608:'ＴＯＫＹＯ　ＭＸ１',
    23609:'ＴＯＫＹＯ　ＭＸ１',
    23610:'ＴＯＫＹＯ　ＭＸ２',
    23615:'ＴＯＫＹＯ　ＭＸ２',
    23992:'ＭＸワンセグ１',
    23993:'ＭＸワンセグ２',
    1088:'放送大学１',
    1089:'放送大学２',
    1090:'放送大学３',
}

# PID
pid_list = {
    0x0: 'PAT',
    0x1: 'CAT',
    0x10: 'NIT',
    0x11: 'SDT/BAT',
    0x12: 'EIT',
    0x26: 'EIT',
    0x27: 'EIT',
    0x13: 'RST',
    0x14: 'TDT/TOT',
    0x17: 'DCT',
    0x1E: 'DIT',
    0x1F: 'SIT',
    0x20: 'LIT',
    0x21: 'ERT',
    0x22: 'PCAT',
    0x23: 'SDTT',
    0x28: 'SDTT',
    0x24: 'BIT',
    0x25: 'NBIT/LDT',
    0x29: 'CDT',
    0x2F: '多重フレームヘッダ',
    0x1FFF: 'Null',
}

table_id = {
    0x00:"PAT",
    0x01:"CAT",
    0x02:"PMT",
    0x3A:"DSM-CCセクション",
    0x3B:"DSM-CCセクション",
    0x3C:"DSM-CCセクション",
    0x3D:"DSM-CCセクション",
    0x3E:"DSM-CCセクション",
    0x3F:"DSM-CCセクション",
    0x40:"NIT（自ネットワーク）",
    0x41:"NIT（他ネットワーク）",
    0x42:"SDT（自ストリーム）",
    0x46:"SDT（他ストリーム）",
    0x4A:"BAT",
    0x4C:"INT",
    0x4E:"EIT（自ストリームの現在と次の番組）",
    0x4F:"EIT（他ストリームの現在と次の番組）",
    0x50:"EIT（自ストリーム、スケジュール）",
    0x51:"EIT（自ストリーム、スケジュール）",
    0x52:"EIT（自ストリーム、スケジュール）",
    0x53:"EIT（自ストリーム、スケジュール）",
    0x54:"EIT（自ストリーム、スケジュール）",
    0x55:"EIT（自ストリーム、スケジュール）",
    0x56:"EIT（自ストリーム、スケジュール）",
    0x57:"EIT（自ストリーム、スケジュール）",
    0x58:"EIT（自ストリーム、スケジュール）",
    0x59:"EIT（自ストリーム、スケジュール）",
    0x5A:"EIT（自ストリーム、スケジュール）",
    0x5B:"EIT（自ストリーム、スケジュール）",
    0x5C:"EIT（自ストリーム、スケジュール）",
    0x5D:"EIT（自ストリーム、スケジュール）",
    0x5E:"EIT（自ストリーム、スケジュール）",
    0x5F:"EIT（自ストリーム、スケジュール）",
    0x60:"EIT（他ストリーム、スケジュール）",
    0x61:"EIT（他ストリーム、スケジュール）",
    0x62:"EIT（他ストリーム、スケジュール）",
    0x63:"EIT（他ストリーム、スケジュール）",
    0x64:"EIT（他ストリーム、スケジュール）",
    0x65:"EIT（他ストリーム、スケジュール）",
    0x66:"EIT（他ストリーム、スケジュール）",
    0x67:"EIT（他ストリーム、スケジュール）",
    0x68:"EIT（他ストリーム、スケジュール）",
    0x69:"EIT（他ストリーム、スケジュール）",
    0x6A:"EIT（他ストリーム、スケジュール）",
    0x6B:"EIT（他ストリーム、スケジュール）",
    0x6C:"EIT（他ストリーム、スケジュール）",
    0x6D:"EIT（他ストリーム、スケジュール）",
    0x6E:"EIT（他ストリーム、スケジュール）",
    0x6F:"EIT（他ストリーム、スケジュール）",
    0x70:"TDT",
    0x71:"RST",
    0x72:"ST",
    0x73:"TOT",
    0x74:"AIT（AITコントロールドアプリケーション）",
    0x75:"AIT（ARIB-J）",
    0x7E:"DIT",
    0x7F:"SIT",
    0x82:"ECM",
    0x83:"ECM",
    0x84:"EMM",
    0x85:"EMM",
    0x87:"DCM",
    0x88:"DCM",
    0x89:"DMM",
    0x8A:"DMM",
    0xC0:"DCT",
    0xC1:"DLT",
    0xC2:"PCAT",
    0xC3:"SDTT",
    0xC4:"BIT",
    0xC5:"NBIT（掲示板情報本体）",
    0xC6:"NBIT（掲示板情報取得のための参照情報）",
    0xC7:"LDT",
    0xC8:"CDT",
    0xD0:"LIT",
    0xD1:"ERT",
    0xD2:"ITT",
    0xFE:"AMT"
}

# 記述子タグ
descriptor_tag = {
    0x04:'階層符号化記述子',
    0x05:'登録記述子',
    0x09:'限定受信方式記述子',
    0x0D:'著作権記述子',
    0x13:'カルーセル識別記述子',
    0x14:'アソシエーションタグ記述子',
    0x15:'拡張アソシエーションタグ記述子',
    0x1C:'MPEG-4 オーディオ記述子',
    0x28:'AVC ビデオ記述子',
    0x2A:'AVC タイミングHRD 記述子',
    0x2E:'MPEG-4 オーディオ拡張記述子',
    0x38:'HEVC ビデオ記述子',
    0x40:'ネットワーク名記述子',
    0x41:'サービスリスト記述子',
    0x42:'スタッフ記述子',
    0x43:'衛星分配システム記述子',
    0x44:'有線分配システム記述子',
    0x47:'ブーケ名記述子',
    0x48:'サービス記述子',
    0x49:'国別受信可否記述子',
    0x4A:'リンク記述子',
    0x4B:'NVOD 基準サービス記述子',
    0x4C:'タイムシフトサービス記述子',
    0x4D:'短形式イベント記述子',
    0x4E:'拡張形式イベント記述子',
    0x4F:'タイムシフトイベント記述子',
    0x50:'コンポーネント記述子',
    0x51:'モザイク記述子',
    0x52:'ストリーム識別記述子',
    0x53:'CA 識別記述子',
    0x54:'コンテント記述子',
    0x55:'パレンタルレート記述子',
    0x58:'ローカル時間オフセット記述子',
    0x63:'パーシャルトランスポートストリーム記述子',
    0x66:'データブロードキャスト識別記述子',
    0x67:'素材情報記述子',
    0x68:'通信連携情報記述子',
    0xBF:'事業者定義記述子のタグ値として選択可能な範囲',
    0xC0:'階層伝送記述子',
    0xC1:'デジタルコピー制御記述子',
    0xC2:'ネットワーク識別記述子',
    0xC3:'パーシャルトランスポートストリームタイム記述子',
    0xC4:'音声コンポーネント記述子',
    0xC5:'ハイパーリンク記述子',
    0xC6:'対象地域記述子',
    0xC7:'データコンテンツ記述子',
    0xC8:'ビデオデコードコントロール記述子',
    0xC9:'ダウンロードコンテンツ記述子',
    0xCA:'CA_EMM_TS 記述子',
    0xCB:'CA 契約情報記述子',
    0xCC:'CA サービス記述子',
    0xCD:'TS 情報記述子',
    0xCE:'拡張ブロードキャスタ記述子',
    0xCF:'ロゴ伝送記述子',
    0xD0:'基本ローカルイベント記述子',
    0xD1:'リファレンス記述子',
    0xD2:'ノード関係記述子',
    0xD3:'短形式ノード情報記述子',
    0xD4:'STC 参照記述子',
    0xD5:'シリーズ記述子',
    0xD6:'イベントグループ記述子',
    0xD7:'SI 伝送パラメータ記述子',
    0xD8:'ブロードキャスタ名記述子',
    0xD9:'コンポーネントグループ記述子',
    0xDA:'SI プライムTS 記述子',
    0xDB:'掲示板情報記述子',
    0xDC:'LDT リンク記述子',
    0xDD:'連結送信記述子',
    0xDE:'コンテント利用記述子',
    0xE0:'サービスグループ記述子',
    0xE1:'エリア放送情報記述子',
    0xE2:'ネットワークダウンロードコンテンツ記述子',
    0xE3:'ダウンロード保護記述子',
    0xE4:'CA 起動記述子',
    0xF3:'有線複数搬送波伝送分配システム記述子',
    0xF4:'高度有線分配システム記述子',
    0xF5:'スクランブル方式記述子',
    0xF6:'アクセス制御記述子',
    0xF7:'カルーセル互換複合記述子',
    0xF8:'限定再生方式記述子',
    0xF9:'有線TS 分割システム記述子',
    0xFA:'地上分配システム記述子',
    0xFB:'部分受信記述子',
    0xFC:'緊急情報記述子',
    0xFD:'データ符号化方式記述子',
    0xFE:'システム管理記述子'
}

def isEit(bit):
    bit = hex(bit)
    return bit == 0x12 or bit == 0x26 or bit == 0x27


class TsFile:
    __read_length = 188
    __read_length_byte = __read_length * 8
    def __init__(self, file=None, offset=0):
        self.__stream = bitstring.ConstBitStream(filename=file)
        self.__stream.pos += self.__read_length_byte * offset
        self.headers = []
        self.payloads = []
    def read(self, packet_count=0): 
        if packet_count == 0 : packet_count = len(self.__stream)
        for i in range(0,packet_count,1):
            now = self.__stream.read(self.__read_length_byte)
            head , payload = now.unpack('bits:40, bits')
            head = TsHeader(head)
            self.headers.append(head)
            if head.payload_unit_start_indicator:
                if isEit(head.pid):
                    self.payloads.append(TsPayload(payload))
                else:
                    self.payloads.append(TsEitPayload(payload))
            else:
                self.payloads.append(TsSequencePayload(payload))

class TsHeader:
    def __init__(self,bits=None):
        self.sync_byte,self.transport_error_indicator,\
        self.payload_unit_start_indicator,self.transport_priority,\
        self.pid,self.transport_scrambling_control,self.adaptation_field_control,\
        self.continuity_counter = bits.unpack('bits:8, bool, bool, bool, uint:13, bits:2, bits:2, bits:4, pad:8')

class TsPayload:
    def __init__(self,bits=None):
        self.payload = bits.unpack('bits')[0]
        pass
    pass

class TsEitPayload(TsPayload):
    def __init__(self, bits=None):
        TsPayload.__init__(self, bits=bits)
        self.table,self.section_syntax_indicator,self.reserved_future_use,self.reserved,self.section_length,self.service_id,\
        self.reserved,self.version_number,self.current_next_indicator,self.section_number,self.last_section_number,\
        self.transport_stream_id,self.original_network_id,self.segment_last_section_number,self.last_table_id, self.data \
        = self.payload.unpack('bits:8 ,bits:1 ,bits:1 ,bits:2 ,bits:12 ,bits:16 ,bits:2, bits:5 ,bits:1 ,bits:8 ,bits:8 ,bits:16 ,bits:16 ,bits:8 ,bits:8, bits')

class TsSequencePayload:
    def __init__(self, bits=None):
        self.data = bits

class TsEitData(TsEitPayload):
    def __init__(self, bits=None):
        TsEitPayload.__init__(self,bits=bits)
        if (self.section_length.uint-11) > 4: # CRCのみのデータでなければ
            self.event_id,self.start_time,self.duration,self.running_status,\
            self.free_CA_mode,self.descriptors_loop_length,self.descriptors = self.data.unpack('bits:16,bits:40,bits:24,bits:3,bits:1,bits:12,bits')
            print(self.event_id,self.start_time,self.duration,self.running_status,\
            self.free_CA_mode,self.descriptors_loop_length)

class TsDescriptorData(TsEitData):
    def __init__(self, bits=None):
        TsEitData.__init__(self,bits=bits)
        if (self.section_length.uint-11) > 4: # CRCのみのデータでなければ
            self.descriptor_tag, self.descriptors_length ,lang,eventname_langth,eventname= self.descriptors.unpack('bits:8,bits:8,bits:24,bits:8,bits')
            print('\n',descriptor_tag[self.descriptor_tag.uint], '記述子長さ:', self.descriptors_length.uint,'バイト')
            if self.descriptor_tag.uint == 0x4D and self.table.uint == 0x4E: # 短形式イベント記述子 かつ EIT（自ストリームの現在と次の番組）
                # 短形式イベント記述子のパース - start クラス化する予定
                print('ながさ',eventname_langth.uint)
                data , text_length, text_char = eventname.unpack(f'bits:{eventname_langth.uint*8},bits:8,bits')
                char = text_char.unpack(f'bits:{text_length.uint*8}')[0]
                print(AribString(data.readlist('uint:8,'*(eventname_langth.uint))).convert_utf(),'\n')
                print(AribString(char.readlist('uint:8,'*(text_length.uint))).convert_utf(),'\n')
                # 短形式イベント記述子のパース - end

file = TsFile(file='D:\Tv_rec\[新]Ｄｒ．ＳＴＯＮＥ　＃１「ＳＴＯＮＥ　ＷＯＲＬＤ」.ts')
file.read(packet_count=10000)

i = 0
put = []
for x in file.headers:
    if ((x.pid == 0x12)): # PID EIT 0x12ペイロード
        payload = file.payloads[i]
        print("\n",hex(x.pid))
        print('セクション先頭:',x.payload_unit_start_indicator)
        print('アダプテーション領域の有無:',x.adaptation_field_control)
        print('transport_priority:',x.transport_priority)
        print('PIDカウンター:',x.continuity_counter.uint)
        print('HEADER raw:',x.sync_byte,x.transport_error_indicator,\
        x.payload_unit_start_indicator,x.transport_priority,\
        x.pid,x.transport_scrambling_control,x.adaptation_field_control,\
        x.continuity_counter)
        if x.payload_unit_start_indicator: # パケットがペイロードの初めのデータである
            count = int(payload.section_length.uint / 184)
            print('分割されたパケット数:',count)
            print('EIT テーブルID:', table_id[payload.table.uint])
            print('EIT LASTテーブルID:', table_id[payload.last_table_id.uint])
            print('EIT サービスID:', payload.service_id.uint)
            print('EIT ネットワークID:', payload.original_network_id)
            print('EIT TSID:', payload.transport_stream_id.uint)
            print('EIT data領域長さ:', payload.section_length.uint-11,'バイト',  (payload.section_length.uint-11)*8,'ビット')
            print('EIT data:', hex(payload.data.uint))
            print(payload.table,payload.section_syntax_indicator,payload.reserved_future_use,payload.reserved,payload.section_length,payload.service_id,\
            payload.reserved,payload.version_number,payload.current_next_indicator,payload.section_number,payload.last_section_number,\
            payload.transport_stream_id,payload.original_network_id,payload.segment_last_section_number,payload.last_table_id)
            put.append(payload.payload.hex)
        else:
            put[len(put)-1] += (payload.data.hex)
            payload = None

    i += 1



for x in put:
    TsDescriptorData(bitstring.ConstBitStream('0x'+ x))

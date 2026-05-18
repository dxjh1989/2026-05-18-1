<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>星區總督指揮面板 - 帝國崛起</title>
    <style>
        body {
            background-color: #0b0f19;
            color: #00ffcc;
            font-family: 'Courier New', Courier, monospace;
            padding: 20px;
            line-height: 1.6;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            border: 1px solid #00ffcc;
            padding: 20px;
            box-shadow: 0 0 15px rgba(0, 255, 204, 0.3);
            border-radius: 8px;
            background: linear-gradient(180deg, #111a2e 0%, #0b0f19 100%);
        }
        h1 {
            text-align: center;
            border-bottom: 2px solid #00ffcc;
            padding-bottom: 10px;
            text-shadow: 0 0 10px #00ffcc;
        }
        .stats {
            display: flex;
            justify-content: space-between;
            background-color: rgba(0, 255, 204, 0.1);
            padding: 15px;
            border-radius: 5px;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .event-box {
            background-color: rgba(255, 255, 255, 0.05);
            padding: 15px;
            border-left: 4px solid #ffcc00;
            margin-bottom: 20px;
            color: #e0e0e0;
        }
        .event-title {
            color: #ffcc00;
            font-size: 1.2em;
            margin-bottom: 10px;
        }
        .options {
            list-style-type: none;
            padding: 0;
        }
        .options li {
            background-color: #1a2639;
            margin-bottom: 10px;
            padding: 10px 15px;
            border: 1px solid #334b6b;
            border-radius: 4px;
            cursor: pointer;
            transition: all 0.3s;
        }
        .options li:hover {
            background-color: #00ffcc;
            color: #0b0f19;
            font-weight: bold;
        }
        .btn-custom {
            display: block;
            width: 100%;
            background: transparent;
            color: #00ffcc;
            border: 1px dashed #00ffcc;
            padding: 10px;
            margin-top: 15px;
            text-align: center;
            border-radius: 4px;
            cursor: pointer;
        }
        .btn-custom:hover {
            background-color: rgba(0, 255, 204, 0.2);
        }
    </style>
</head>
<body>

<div class="container">
    <h1>=== 第 1 回合 ===</h1>
   
    <div class="stats">
        <span>⚔️ 軍事: 50</span>
        <span>💰 經濟: 50</span>
        <span>🤝 民心: 50</span>
        <span>🔬 科技: 50</span>
        <span>🗺️ 領土: 50</span>
    </div>

    <div class="event-box">
        <div class="event-title">📜 【局勢與事件：碎星帶的危機】</div>
        <p>指揮官，歡迎來到「新星」邊境星區。深空探測站發來緊急警報：在邊境無人區「碎星帶」捕捉到異星求救訊號，並發現豐富的「零號元素」礦脈。然而，「猩紅之刃」星際海盜艦隊正在向該區域集結，打算劫掠資源並攔截訊號。</p>
    </div>

    <h2 style="font-size: 1.2em; color: #fff;">🎯 請下達指令：</h2>
    <ul class="options">
        <li>[A] 派遣星際艦隊前往鎮壓海盜並調查訊號 (預期：引發交火，可能擴張領土與獲得科技)</li>
        <li>[B] 秘密派遣重型採礦船前往邊緣偷採資源 (預期：獲得經濟收益，但平民有被襲擊風險)</li>
        <li>[C] 封鎖邊境，升級星區行星防禦矩陣 (預期：提升科技與防禦，錯失良機影響民心)</li>
    </ul>
   
    <button class="btn-custom">[D] 自定義指令 (開啟通訊終端輸入對策)</button>
</div>

</body>
</html>

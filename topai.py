import sqlite3
import webbrowser
import time

def pasiekimu_sk(string):
    return len(string)-1

def topai():

    conn = sqlite3.connect("data.db")
    c = conn.cursor()

    c.execute("SELECT * FROM paskyros ORDER BY lygis DESC LIMIT 10")
    data = c.fetchall()

    conn.commit()
    conn.close()
    



    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8" />
            <title>Greiti pirstai TOP 10</title>
            <link rel="stylesheet" href="./style.css" />
        </head>
        <body>
            <div class="container">
            <div class="table">
                <div class="table-header">
                <div class="header-item">
                    <p class="filter-link">Nr.</p>
                </div>
                <div class="header-item">
                    <p class="filter-link">Vardas</p>
                </div>
                <div class="header-item">
                    <p class="filter-link">Lygis</p>
                </div>
                <div class="header-item">
                    <p class="filter-link">Pasiekimu sk.</p>
                </div>
                <div class="header-item">
                    <p class="filter-link">Patirtis</p>
                </div>
                </div>
                <div class="table-content">
                <div class="table-row">
                    <div class="table-data">1</div>
                    <div class="table-data">{data[0][0]}</div>
                    <div class="table-data">{data[0][2]}</div>
                    <div class="table-data">{pasiekimu_sk(data[0][3])}</div>
                    <div class="table-data">{data[0][4]}</div>
                </div>
                <div class="table-row">
                    <div class="table-data">2</div>
                    <div class="table-data">{data[1][0]}</div>
                    <div class="table-data">{data[1][2]}</div>
                    <div class="table-data">{pasiekimu_sk(data[1][3])}</div>
                    <div class="table-data">{data[1][4]}</div>
                </div>
                <div class="table-row">
                    <div class="table-data">3</div>
                    <div class="table-data">{data[2][0]}</div>
                    <div class="table-data">{data[2][2]}</div>
                    <div class="table-data">{pasiekimu_sk(data[2][3])}</div>
                    <div class="table-data">{data[2][4]}</div>
                </div>
                <div class="table-row">
                    <div class="table-data">4</div>
                    <div class="table-data">{data[3][0]}</div>
                    <div class="table-data">{data[3][2]}</div>
                    <div class="table-data">{pasiekimu_sk(data[3][3])}</div>
                    <div class="table-data">{data[3][4]}</div>
                </div>
                <div class="table-row">
                    <div class="table-data">5</div>
                    <div class="table-data">{data[4][0]}</div>
                    <div class="table-data">{data[4][2]}</div>
                    <div class="table-data">{pasiekimu_sk(data[4][3])}</div>
                    <div class="table-data">{data[4][4]}</div>
                </div>
                <div class="table-row">
                    <div class="table-data">6</div>
                    <div class="table-data">{data[5][0]}</div>
                    <div class="table-data">{data[5][2]}</div>
                    <div class="table-data">{pasiekimu_sk(data[5][3])}</div>
                    <div class="table-data">{data[5][4]}</div>
                </div>
                <div class="table-row">
                    <div class="table-data">7</div>
                    <div class="table-data">{data[6][0]}</div>
                    <div class="table-data">{data[6][2]}</div>
                    <div class="table-data">{pasiekimu_sk(data[6][3])}</div>
                    <div class="table-data">{data[6][4]}</div>
                </div>
                <div class="table-row">
                    <div class="table-data">8</div>
                    <div class="table-data">{data[7][0]}</div>
                    <div class="table-data">{data[7][2]}</div>
                    <div class="table-data">{pasiekimu_sk(data[7][3])}</div>
                    <div class="table-data">{data[7][4]}</div>
                </div>
                <div class="table-row">
                    <div class="table-data">9</div>
                    <div class="table-data">{data[8][0]}</div>
                    <div class="table-data">{data[8][2]}</div>
                    <div class="table-data">{pasiekimu_sk(data[8][3])}</div>
                    <div class="table-data">{data[8][4]}</div>
                </div>
                <div class="table-row">
                    <div class="table-data">10</div>
                    <div class="table-data">{data[9][0]}</div>
                    <div class="table-data">{data[9][2]}</div>
                    <div class="table-data">{pasiekimu_sk(data[9][3])}</div>
                    <div class="table-data">{data[9][4]}</div>
                </div>
                </div>
            </div>
            </div>
        </body>
    </html>
    """


    with open("index.html", "w") as html_file:
        html_file.write(html_content)

    time.sleep(2)
    webbrowser.open_new_tab("index.html")

 

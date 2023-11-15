from bs4 import BeautifulSoup
# import requests


html_content="""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>

<head>
    <meta http-equiv="Content-type" content="text/html; charset=utf-8">
    <link rel="shortcut icon" type="image/x-icon" href="favicon.ico">
    <title>OnionLinks</title>
    <style type="text/css">
        body {
            background: #FFF;
            color: #000;
            margin: 0;
            padding: 0
        }

        body,
        .buttn,
        .txt,
        textarea,
        #menu a {
            font: 13px Verdana, Tahoma, serif
        }

        div {
            position: relative
        }

        :focus {
            outline: none
        }

        ::-moz-focus-inner {
            border: 0
        }

        #logo {
            height: calc(10vw);
            left: 0px;
            margin-left: 0px;
            background-size: contain;
            background-repeat: no-repeat;
            background-image: url("logo.png")
        }

        #main {
            -moz-border-radius: 15px;
            -webkit-border-radius: 15px;
            border: 3px dotted #D5DDEB;
            border-radius: 15px;
            left: 5px;
            word-wrap: break-word;
            width: 100%
        }

        .buttn {
            height: 30px
        }

        .buttn,
        #menu a,
        .txt,
        textarea,
        .floatimg {
            -moz-box-shadow: 2px 2px 2px rgba(0, 0, 0, 0.333);
            -webkit-box-shadow: 2px 2px 2px rgba(0, 0, 0, 0.333);
            box-shadow: 2px 2px 2px rgba(0, 0, 0, 0.333);
        }

        .txt {
            height: 24px;
            margin: 4px 0;
            text-align: center
        }

        textarea {
            overflow: auto;
            padding: 8px
        }

        .txt,
        textarea,
        .floatimg {
            background: #555;
            border: 2px outset #555;
            color: #FFF
        }

        .txt:focus,
        textarea:focus {
            background: #111;
            border: 2px outset #111
        }

        input.checkb {
            margin-top: 15px
        }

        a:link {
            font-size: 16px;
            text-decoration: none
        }

        strong {
            font-size: 22px;
            color: #000
        }

        a:link,
        #warning {
            color: blue;
            font-weight: 700
        }

        a:link,
        h3 {
            font-family: Constantia, Georgia, serif
        }

        a:hover,
        a:focus {
            color: #333
        }

        #checkout {
            font-size: 30px
        }

        h3 {
            color: #395379;
            font-size: 28px;
            font-style: italic;
            line-height: 9px
        }

        h3,
        #footertext,
        #menu a,
        .buttn {
            text-shadow: 0 1px 1px rgba(0, 0, 0, 0.333);
        }

        hr {
            background-image: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA1IAAAADBAMAAABrMiP7AAAAK3RFWHRDcmVhdGlvbiBUaW1lAG5lZCAzIG+edSAyMDEzIDE5OjE2OjA3ICswMTAwRdOxOQAAAAd0SU1FB90DAxIRNFqu0NQAAAAJcEhZcwAACxIAAAsSAdLdfvwAAAAEZ0FNQQAAsY8L/GEFAAAAFVBMVEX6+/3c4+7////t8ffV3evu8ffd4+9BbIVwAAAAH0lEQVR42mNgS1AaRUMBMZi4Ko2ioYAYGAWURtFQQAD+UL1PuIeVRwAAAABJRU5ErkJggg==);
            height: 3px
        }

        hr,
        img {
            border: 0
        }

        .table1 td,
        .table1 th {
            padding: 5px 7px;
            text-align: left
        }

        .table1 th {
            border: 3px dotted #D5DDEB
        }

        .table1 td {
            background: #EEF1F6
        }

        .floatimg {
            margin: 0 19px 19px 0
        }

        #footer {
            height: 60px;
        }

        #footertext {
            font-size: 11px;
            text-align: center;
            top: 29px;
        }
    </style>
</head>

<body>
    <div id="main">
        <div id="logo"></div>
        <hr>
        <!-- EVERYTHING ABOVE THIS LINE CAN BE CHANGED --><!-- EVERYTHING ABOVE THIS LINE CAN BE CHANGED --><!-- EVERYTHING ABOVE THIS LINE CAN BE CHANGED --><!-- EVERYTHING ABOVE THIS LINE CAN BE CHANGED --><!-- EVERYTHING ABOVE THIS LINE CAN BE CHANGED -->
        <h3>OnionLinks</h3>Short .onion v2 websites will stop working in October 2021.<a href="#Others">Others</a></p>
        <p>&nbsp;</p>
        <h2 id="Introduction">Introduction Points</h2>
        <p><a href="http://s4k4ceiapwwgcm3mkb6e4diqecpo7kvdnfr5gg7sph7jjppqkvwwqtyd.onion/" target="_blank"
                rel="nofollow noreferrer noopener"><strong>On<a
                        href="http://2jwcnprqbugvyi6ok2h2h7u26qc6j5wxm7feh3znlh2qu3h6hjld4kyd.onion/" target="_blank"
                        rel="nofollow noreferrer noopener"><strong>Another Hidden Wiki</strong>
                        2jwcnprqbugvyi6ok2h2h7u26qc6j5wxm7feh3znlh2qu3h6hjld4kyd.onion</a>
                    <<a href="http://zqktlwiuavvvqqt4ybvgvi7tyo4hjl5xgfuvpdf6otjiycgwqbym2qad.onion/wiki/index.php/Main_Page"
                        target="_blank" rel="nofollow noreferrer noopener"><strong>The Original Hidden Wiki</strong>
                        zqktlwiuavvvqqt4ybvgvi7tyo4hjl5xgfuvpdf6otjiycgwqbym2qad.onion</a></p>
        <p>&nbsp;</p>
        <h2 id="Financial">Financial Services</h2>
        <p><a href="http://55niksbd22qqaedkw36qw4cpofmbxdtbwonxam7ov2ga62zqbhgty3yd.onion/" target="_blank"
                rel="nofollow noreferrer noopener"><strong>AccMar<a
                        href="http://hqfld5smkr4b4xrjcco7zotvoqhuuoehjdvoin755iytmpk4sm7cbwad.onion/" target="_blank"
                        rel="nofollow noreferrer noopener"><strong>Mixabit Bitcoin Mixer</strong>
                        hqfld5smkr4b4xrjcco7zotvoqhuuoehjdvoin755iytmpk4sm7cbwad.onion</a<a
                            href="http://mp3fpv6xbrwka4skqliiifoizghfbjy5uyu77wwnfruwub5s4hly2oid.onion/"
                            target="_blank" rel="nofollow noreferrer noopener"><strong>EasyCoin Bitcoin Mixer</strong>
                        mp3fpv6xbrwka4skqliiifoizghfbjy5uyu77wwnfruwub5s4hly2oid.onion</<a
                            href="http://p2qzxkca42e3wccvqgby7jrcbzlf6g7pnkvybnau4szl5ykdydzmvbid.onion/"
                            target="_blank" rel="nofollow noreferrer noopener"><strong>Onionwallet Bitcoin
                            Mixer</strong> p2qzxkca42e3wccvqgby7jrcbzlf6g7pnkvybnau4szl5ykdydzmvbid.onion</a></p>
        <p>&nbsp;</p>
        <h2 id="Commercial">Commercial Services</h2>
        <p><a href="http://prjd5pmbug2cnfs67s3y65ods27vamswdaw2lnwf45ys3pjl55h2gwqd.onion/" target="_blank"
                rel="nofollow noreferrer noopener"><strong>DarkWebHackers</strong> prj<a
                    href="http://vhlehwexxmbnvecbmsk4ormttdvhlhbnyabai4cithvizzaduf3gmayd.onion/" target="_blank"
                    rel="nofollow noreferrer noopener"><strong>Kamagra 4 Bitcoin</strong>
                    vhlehwexxmbnvecbmsk4ormttdvhlhbnyabai4cithvizzaduf3gmayd.onion</a>
                <br<a href="http://ymvhtqya23wqpez63gyc3ke4svju3mqsby2awnhd3bk2e65izt7baqad.onion/" target="_blank"
                    rel="nofollow noreferrer noopener"><strong>OnionIdentityServices</strong>
                    ymvhtqya23wqpez63gyc3ke4svju3mqsby2awnhd3bk2e65izt7baqad.onion</a<a
                        href="http://kq4okz5kf4xosbsnvdr45uukjhbm4oameb6k6agjjsydycvflcewl4qd.onion/" target="_blank"
                        rel="nofollow noreferrer noopener"><strong>Rent-A-Hacker</strong>
                    kq4okz5kf4xosbsnvdr45uukjhbm4oameb6k6agjjsydycvflcewl4qd.onion
            </a></p>
        <p>&nbsp;</p>
        <h2 id="Drugs">Drugs</h2>
        <p><a href="http://wbz2lrxhw4dd7h5t2wnoczmcz5snjpym4pr7dzjmah4vi6yywn37bdyd.onion/" target="_blank"
                rel="nofollow noreferrer noopener"><strong>DCdutchconnectionUK</strong> wbz2lrxhw4dd7h5t2wnoczmcz5snj<a
                    href="http://xf2gry25d3tyxkiu2xlvczd3q7jl6yyhtpodevjugnxia2u665asozad.onion/" target="_blank"
                    rel="nofollow noreferrer noopener"><strong>Peoples Drug Store</strong>
                    xf2gry25d3tyxkiu2xlvczd3q7jl6yyhtpodevjugnxia2u665asozad.onion</a>
                <b<a href="http://7sk2kov2xwx6cbc32phynrifegg6pklmzs7luwcggtzrnlsolxxuyfyd.onion/en/index.html"
                    target="_blank" rel="nofollow noreferrer noopener"><strong>SystemLi.org</strong>
                    7sk2kov2xwx6cbc32phynrifegg6pklmzs7luwcggtzrnlsolxxuyfyd.onio<a
                        href="http://sonarmsng5vzwqezlvtu2iiwwdn3dxkhotftikhowpfjuzg7p3ca5eid.onion/" target="_blank"
                        rel="nofollow noreferrer noopener"><strong>Sonar Tor Messenger</strong>
                        sonarmsng5vzwqezlvtu2iiwwdn3dxkhotftikhowpfjuzg7p3ca5eid.onion</a>
                    <<a href="http://meynethaffeecapsvfphrcnfrx44w2nskgls2juwitibvqctk2plvhqd.onion/" target="_blank"
                        rel="nofollow noreferrer noopener"><strong>MayVaneDay Studios</strong>
                        meynethaffeecapsvfphrcnfrx44w2nskgls2juwitibvqctk2plvhqd.onion
            </a>
            <b<a href="http://lpiyu33yusoalp5kh3f4hak2so2sjjvjw5ykyvu2dulzosgvuffq6sad.onion/" target="_blank"
                rel="nofollow noreferrer noopener"><strong>Tech Learning Collective</strong>
                lpiyu33yusoalp5kh3f4hak2so2sjjvjw5ykyvu2dulzosgvuffq6sad.onion<a
                    href="http://nv3x2jozywh63fkohn5mwp2d73vasusjixn3im3ueof52fmbjsigw6ad.onion/" target="_blank"
                    rel="nofollow noreferrer noopener"><strong>Comic Book Library</strong>
                    nv3x2jozywh63fkohn5mwp2d73vasusjixn3im3ueof52fmbjsigw6ad.onion</a>
                <b<a href="http://libraryfyuybp7oyidyya3ah5xvwgyx6weauoini7zyz555litmmumad.onion/" target="_blank"
                    rel="nofollow noreferrer noopener"><strong>Just Another Library</strong>
                    libraryfyuybp7oyidyya3ah5xvwgyx6weauoini7zyz555litmmumad.onion</a><a
                        href="http://ncidetfs7banpz2d7vpndev5somwoki5vwdpfty2k7javniujekit6ad.onion/" target="_blank"
                        rel="nofollow noreferrer noopener"><strong>NCIDE Police Task Force</strong>
                        ncidetfs7banpz2d7vpndev5somwoki5vwdpfty2k7javniujekit6ad.onion<<a
                            href="http://he5dybnt7sr6cm32xt77pazmtm65flqy6irivtflruqfc5ep7eiodiad.onion/"
                            target="_blank" rel="nofollow noreferrer noopener"><strong>Rewards For Justice</strong>
                            he5dybnt7sr6cm32xt77pazmtm65flqy6irivtflruqfc5ep7eiodiad.onion</a>
                    <<a href="http://spore64i5sofqlfz5gq2ju4msgzojjwifls7rok2cti624zyq3fcelad.onion/" target="_blank"
                        rel="nofollow noreferrer noopener"><strong>SporeStack Hosting</strong>
                        spore64i5sofqlfz5gq2ju4msgzojjwifls7rok2cti624zyq3fcelad.onion</a>
                        <b<a href="http://explorerzydxu5ecjrkwceayqybizmpjjznk5izmitf2modhcusuqlid.onion/"
                            target="_blank" rel="nofollow noreferrer noopener"><strong>Blockstream BTC Explorer</strong>
                            explorerzydxu5ecjrkwceayqybizmpjjznk5izmitf2modhcusuqlid.onion<a
                                href="http://blkchairbknpn73cfjhevhla7rkp4ed5gg2knctvv7it4lioy22defid.onion/"
                                target="_blank" rel="nofollow noreferrer noopener"><strong>BlockChair BTC
                                    Explorer</strong> blkchairbknpn73cfjhevhla7rkp4ed5gg2knctvv7it4lioy22defid.onion<<a
                                    href="http://bombsjy5lsgehdyuevxu5kt3zdw22bfqrhbanc32evab3o3j3dvc7cid.onion/"
                                    target="_blank" rel="nofollow noreferrer noopener"><strong>Shitposting
                                        Forum</strong>
                                    bombsjy5lsgehdyuevxu5kt3zdw22bfqrhbanc32evab3o3j3dvc7cid.onion</a>
                            <br<a href="http://jptvwdeyknkv6oiwjtr2kxzehfnmcujl7rf7vytaikmwlvze773uiyyd.onion/"
                                target="_blank" rel="nofollow noreferrer noopener"><strong>The Longest Onion
                                    Index</strong> jptvwdeyknkv6oiwjtr2kxzehfnmcujl7rf7vytaikmwlvze773uiyyd.onion<<!--
                                    EVERYTHING BELOW THIS LINE CAN BE CHANGED
                                    --><!-- EVERYTHING BELOW THIS LINE CAN BE CHANGED --><!-- EVERYTHING BELOW THIS LINE CAN BE CHANGED --><!-- EVERYTHING BELOW THIS LINE CAN BE CHANGED -->
                                    <div id="footer">
                                        <div id="footertext">OnionLinks</div>
                                    </div>
    </div>
</body>

</html>"""



def extract_href_links(html_content):
    links = []
    soup = BeautifulSoup(html_content, 'html.parser')
    for a_tag in soup.find_all('a', href=True):
        links.append(a_tag['href'])
    return links

# # Example usage:
# url = 'https://example.com'
# response = requests.get(url)
# html_content = response.text

href_links = extract_href_links(html_content)

print("Extracted HREF links:")
for link in href_links:
    print(link)

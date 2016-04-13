# coding:utf8
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
    
    def collect_data(self, data):
        if data is None:
            print("data is None")
            return
        self.datas.append(data)

    
    def output_html(self):
        fout = open('output.html', 'w')
        fout.write("<html><head><meta charset='utf8'><style>td{border:1px solid #000}</style></head>")
        fout.write("<body>")
        fout.write("<table CELLPADDING='5' CELLSPACING='5'>")
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>"%(data['url']))
            fout.write("<td>%s</td>"%(data['title'].encode('utf8')))
            fout.write("<td>%s</td>"%(data['summary'].encode('utf8')))
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</body>")
        pass
    
    
    
    




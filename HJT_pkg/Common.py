
class CommonClass:
    def createEnvironmentFile(self, file, string):
        content1="<environment>\n   <parameter>\n       <key>HexmeetHJT.version</key>\n     <value>"
        content2="</value>\n    </parameter>\n</environment>"

        with open(file, "w+") as f:
            f.truncate()
            f.write(content1+string+content2)



if __name__ == '__main__':
    CommonClass().createEnvironmentFile("../test/allure-results/Environment.xml","1.4.1.157")

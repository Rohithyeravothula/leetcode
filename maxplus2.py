class Solution(object):
    def orderOfLargestPlusSign(self, l, mines_matrix):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        def printMatrix(matrix):
            for o in matrix:
                print(o)
            print("\n\n")
        if l == 0:
            return 0

        mines = [[1]*l for _ in xrange(0, l)]
        for i,j in mines_matrix:
            mines[i][j] = 0

        row_back = [[0]*(l) for _ in xrange(0, l)]
        row_forward = [[0]*(l) for _ in xrange(0, l)]

        col_back = [[0]*l for _ in xrange(0, l)]
        col_forward = [[0]*l for _ in xrange(0, l)]

        for i in xrange(0, l):
            row_back[i][0] = mines[i][0]
            for j in xrange(1, l):
                if mines[i][j] == 0:
                    row_back[i][j] = 0
                else:
                    row_back[i][j] = 1+row_back[i][j-1]
            
            row_forward[i][l-1] = mines[i][l-1]
            for j in xrange(l-2, -1, -1):
                if mines[i][j]== 0:
                    row_forward[i][j] = 0
                else:
                    row_forward[i][j] = 1+row_forward[i][j+1]

        for j in xrange(0, l):
            col_back[0][j]=mines[0][j]
            for i in xrange(1, l):
                if mines[i][j] == 0:
                    col_back[i][j] = 0
                else:
                    col_back[i][j] = 1+col_back[i-1][j]

            col_forward[l-1][j] = mines[l-1][j]
            for i in xrange(l-2, -1, -1):
                if mines[i][j] == 0:
                    col_forward[i][j]=0
                else:
                    col_forward[i][j] = 1+col_forward[i+1][j]

        # printMatrix(mines)
        # printMatrix(row_back)
        # printMatrix(row_forward)
        # printMatrix(col_back)
        # printMatrix(col_forward)
        maxorder = 0
        for i in xrange(1, l-1):
            for j in xrange(1, l-1):
                if mines[i][j] == 1:
                    curmax = 1+min(min(row_back[i][j-1], row_forward[i][j+1]), min(col_back[i-1][j], col_forward[i+1][j]))
                    maxorder = max(curmax, maxorder)

        for i in xrange(0, l):
            maxorder = max(maxorder, mines[i][0])
            maxorder = max(maxorder, mines[0][i])
            maxorder = max(maxorder, mines[i][l-1])
            maxorder = max(maxorder, mines[l-1][i])
        return maxorder



#mtrix = [[0,307],[0,308],[0,421],[1,12],[1,79],[1,142],[1,218],[1,351],[1,365],[1,389],[1,493],[2,133],[2,290],[2,323],[2,377],[2,444],[3,63],[3,202],[3,207],[3,230],[3,252],[3,266],[3,434],[3,480],[4,0],[4,130],[4,304],[5,14],[5,55],[5,108],[5,118],[5,199],[5,205],[5,336],[5,466],[6,67],[6,74],[6,131],[6,183],[6,235],[6,309],[6,405],[6,408],[6,428],[6,491],[7,178],[7,249],[7,378],[7,398],[8,118],[8,202],[8,232],[8,273],[8,342],[8,375],[8,446],[8,478],[9,18],[9,233],[9,324],[9,342],[9,399],[9,458],[10,32],[10,61],[10,146],[10,160],[10,210],[10,368],[10,373],[11,54],[11,65],[11,76],[11,99],[11,129],[11,132],[11,143],[11,163],[11,211],[11,233],[11,242],[11,317],[12,152],[12,227],[12,397],[12,402],[12,444],[12,450],[12,458],[13,307],[13,330],[13,420],[13,438],[14,43],[14,103],[14,112],[14,152],[14,196],[14,201],[14,234],[14,312],[14,337],[14,415],[15,0],[15,139],[15,251],[15,276],[15,304],[15,432],[15,499],[16,32],[16,79],[16,217],[16,317],[16,359],[16,362],[16,387],[16,401],[17,100],[17,198],[17,305],[18,63],[18,110],[18,256],[18,309],[18,316],[18,321],[18,384],[18,477],[19,55],[19,120],[19,139],[19,276],[19,299],[19,306],[19,342],[19,385],[19,433],[19,496],[20,12],[20,179],[20,220],[20,258],[20,281],[20,337],[20,479],[21,220],[21,263],[21,266],[21,299],[22,39],[22,161],[22,238],[22,247],[22,286],[23,6],[23,135],[23,168],[23,239],[23,408],[23,451],[23,469],[24,40],[24,122],[24,146],[24,284],[24,455],[25,16],[25,46],[25,64],[25,171],[25,172],[25,203],[25,214],[25,237],[25,250],[25,290],[25,327],[25,381],[26,57],[26,60],[26,144],[26,435],[26,476],[27,218],[27,232],[27,236],[27,249],[27,339],[27,469],[28,31],[28,68],[28,141],[28,173],[28,249],[28,304],[29,89],[29,113],[30,116],[30,260],[30,411],[30,470],[31,28],[31,45],[31,65],[31,113],[31,226],[31,259],[31,339],[31,484],[32,104],[32,217],[32,225],[32,249],[32,315],[32,360],[32,367],[32,383],[32,429],[33,104],[33,106],[33,144],[33,183],[33,217],[33,227],[33,238],[33,249],[33,349],[33,418],[33,499],[34,88],[34,174],[34,293],[34,369],[35,0],[35,275],[35,387],[35,403],[35,412],[35,474],[36,258],[36,272],[36,356],[36,401],[36,474],[36,496],[37,68],[37,228],[37,272],[37,292],[38,375],[38,402],[38,444],[39,136],[39,180],[39,198],[39,209],[39,227],[39,277],[40,126],[40,203],[40,247],[40,463],[40,496],[41,399],[41,489],[41,499],[42,125],[42,387],[42,395],[42,439],[42,480],[43,114],[43,141],[43,146],[43,371],[43,445],[44,86],[44,283],[44,334],[44,416],[45,13],[45,149],[45,159],[45,186],[45,280],[45,359],[45,390],[45,425],[46,48],[46,52],[46,93],[46,111],[46,118],[46,133],[46,140],[46,167],[46,247],[46,418],[46,424],[47,78],[47,219],[47,249],[47,350],[47,497],[48,104],[48,106],[48,115],[48,345],[48,365],[48,418],[48,499],[49,29],[49,38],[49,104],[49,137],[49,179],[49,277],[49,350],[49,361],[49,416],[50,59],[50,97],[50,141],[50,153],[50,165],[50,296],[50,390],[50,476],[51,88],[51,274],[51,388],[52,75],[52,128],[52,216],[52,411],[53,178],[53,378],[53,494],[54,25],[54,99],[54,282],[54,321],[54,358],[54,452],[55,4],[55,28],[55,62],[55,179],[55,307],[55,406],[55,482],[56,50],[56,82],[56,108],[56,237],[56,256],[56,317],[56,407],[56,424],[57,35],[57,55],[57,203],[57,275],[57,412],[57,460],[58,129],[58,189],[58,206],[58,348],[58,376],[58,411],[59,13],[59,287],[59,420],[59,487],[60,62],[60,168],[60,178],[60,332],[60,341],[60,368],[60,384],[60,385],[60,440],[61,74],[61,94],[61,116],[61,153],[61,284],[61,330],[61,399],[61,409],[62,161],[62,208],[62,275],[62,386],[62,447],[63,79],[63,114],[63,236],[63,265],[63,450],[63,483],[64,4],[64,248],[64,314],[64,358],[64,382],[64,427],[64,435],[65,44],[65,47],[65,71],[65,95],[65,103],[65,252],[65,261],[65,323],[65,457],[65,485],[66,136],[66,224],[66,341],[66,422],[66,481],[67,162],[67,176],[67,273],[67,403],[67,425],[69,59],[69,101],[69,298],[69,328],[69,349],[69,399],[69,466],[70,114],[70,185],[70,244],[70,377],[71,58],[71,73],[71,260],[71,266],[71,363],[71,380],[71,392],[71,455],[72,39],[72,42],[72,152],[72,413],[72,498],[73,22],[73,61],[73,78],[73,162],[73,213],[73,237],[73,293],[73,418],[73,444],[73,453],[74,36],[74,375],[74,379],[74,418],[74,437],[74,469],[75,134],[75,272],[75,406],[77,326],[77,360],[77,426],[77,466],[78,122],[78,343],[78,402],[79,70],[79,83],[79,229],[79,364],[79,388],[79,490],[80,13],[80,319],[80,430],[80,459],[80,466],[80,486],[81,27],[81,286],[81,436],[82,1],[82,172],[82,238],[82,249],[82,441],[82,492],[83,135],[83,494],[84,122],[84,328],[84,377],[84,489],[85,117],[85,157],[85,164],[85,187],[85,331],[85,365],[85,479],[85,485],[86,211],[86,330],[87,53],[87,54],[87,166],[87,270],[88,218],[88,226],[88,289],[88,295],[88,426],[89,30],[89,40],[89,180],[89,200],[89,244],[89,407],[89,465],[90,212],[90,242],[90,287],[90,316],[90,340],[90,364],[91,43],[91,141],[91,159],[91,195],[91,423],[92,61],[92,77],[92,156],[92,184],[92,219],[92,394],[92,412],[92,414],[93,23],[93,178],[93,310],[93,328],[93,356],[93,372],[93,385],[93,420],[93,449],[94,85],[94,94],[94,104],[94,109],[94,147],[94,148],[94,388],[94,450],[95,9],[95,51],[95,62],[95,121],[95,150],[95,214],[95,240],[95,345],[96,18],[96,70],[96,211],[96,274],[96,345],[96,393],[97,51],[97,82],[97,245],[97,361],[97,394],[98,144],[98,175],[98,316],[98,378],[98,465],[99,2],[99,41],[99,103],[99,162],[99,172],[99,440],[99,454],[100,41],[100,95],[100,256],[100,316],[100,339],[100,390],[100,486],[101,419],[101,461],[101,490],[102,68],[102,74],[102,113],[102,190],[102,272],[102,276],[102,363],[102,387],[102,389],[103,84],[103,133],[103,169],[103,264],[103,269],[103,282],[103,310],[103,316],[103,345],[104,401],[104,469],[104,498],[105,227],[105,391],[105,410],[105,426],[106,55],[106,75],[106,103],[106,179],[106,187],[106,192],[106,238],[106,250],[106,337],[106,381],[106,441],[107,153],[107,177],[107,200],[107,214],[107,435],[107,495],[108,89],[108,119],[108,139],[108,266],[108,311],[108,413],[108,427],[108,490],[109,37],[109,38],[109,151],[109,209],[109,417],[109,474],[110,14],[110,15],[110,36],[110,133],[110,152],[110,205],[110,246],[110,264],[110,494],[111,65],[111,117],[112,21],[112,30],[112,56],[112,89],[112,94],[112,114],[112,205],[112,358],[112,369],[112,380],[112,460],[112,475],[113,8],[113,69],[113,101],[113,263],[113,338],[113,438],[114,81],[114,110],[114,144],[114,182],[114,183],[114,351],[114,364],[114,427],[114,450],[114,461],[115,65],[115,136],[115,145],[115,204],[115,221],[115,333],[115,476],[116,59],[116,135],[116,200],[117,194],[117,340],[117,424],[118,121],[118,162],[118,396],[119,111],[119,154],[119,179],[119,231],[119,266],[119,332],[119,368],[119,459],[119,483],[120,17],[120,36],[120,40],[120,60],[120,167],[120,283],[120,284],[120,494],[121,101],[121,166],[121,429],[121,448],[122,127],[122,185],[122,299],[122,369],[122,469],[122,498],[123,48],[123,64],[123,245],[123,290],[124,75],[124,105],[124,202],[124,403],[124,452],[125,163],[125,190],[125,202],[125,208],[125,211],[125,393],[125,419],[125,420],[125,497],[126,52],[126,160],[126,208],[126,242],[126,484],[127,42],[127,62],[127,169],[127,205],[127,238],[127,289],[127,343],[127,364],[127,416],[128,7],[128,72],[128,174],[128,340],[129,12],[129,215],[129,317],[129,331],[129,414],[130,56],[130,84],[130,172],[130,496],[131,80],[131,112],[131,124],[131,142],[132,62],[132,73],[132,93],[132,213],[132,367],[133,17],[133,92],[133,183],[133,231],[133,233],[133,236],[133,302],[133,352],[134,65],[134,162],[134,299],[134,350],[134,392],[134,399],[135,43],[135,79],[135,165],[135,211],[135,229],[136,102],[136,278],[136,286],[136,289],[136,374],[137,51],[137,91],[137,205],[137,368],[137,381],[137,449],[139,159],[139,232],[139,266],[139,405],[140,232],[140,287],[140,299],[140,392],[141,43],[141,62],[141,319],[141,377],[141,408],[141,449],[141,475],[142,5],[142,86],[142,271],[142,361],[142,403],[142,437],[143,35],[143,135],[143,153],[143,220],[143,279],[143,407],[143,481],[144,18],[144,41],[144,42],[144,162],[144,193],[144,244],[144,442],[144,496],[145,25],[145,75],[145,112],[145,268],[145,317],[145,453],[146,20],[146,158],[146,202],[146,263],[146,320],[146,379],[146,407],[147,151],[147,165],[147,179],[147,197],[147,254],[147,373],[147,457],[147,476],[147,489],[148,69],[148,115],[148,176],[148,264],[148,294],[148,334],[148,479],[149,15],[149,63],[149,345],[149,420],[149,458],[150,29],[150,33],[150,62],[150,215],[151,21],[151,158],[151,218],[151,224],[151,234],[151,308],[152,5],[152,138],[152,160],[152,324],[152,454],[153,126],[153,172],[153,202],[153,278],[153,281],[153,308],[153,328],[154,61],[154,151],[154,167],[154,179],[154,216],[154,242],[154,319],[154,402],[154,430],[155,5],[155,72],[155,119],[155,253],[155,289],[156,13],[156,81],[156,120],[156,146],[156,267],[156,282],[156,326],[156,407],[156,457],[156,472],[157,35],[157,328],[157,423],[157,486],[157,487],[158,7],[158,162],[158,201],[158,250],[158,369],[159,95],[159,458],[160,48],[160,148],[160,268],[160,272],[160,280],[160,332],[160,355],[160,443],[160,468],[160,491],[161,10],[161,139],[161,176],[161,231],[161,265],[161,290],[161,293],[161,352],[161,361],[161,401],[161,414],[161,415],[161,478],[162,180],[162,203],[162,287],[162,288],[162,379],[162,404],[162,432],[163,234],[163,354],[163,380],[163,419],[164,44],[164,118],[164,134],[164,226],[164,374],[164,394],[165,34],[165,110],[165,118],[165,329],[165,401],[165,426],[165,433],[166,29],[166,53],[166,77],[166,85],[166,98],[166,296],[166,338],[166,345],[167,218],[167,242],[167,248],[167,322],[167,353],[167,412],[167,483],[168,4],[168,127],[168,138],[168,199],[168,268],[168,304],[168,386],[168,459],[169,11],[169,28],[169,46],[169,229],[169,458],[170,60],[170,121],[170,198],[170,244],[170,315],[170,388],[170,466],[171,38],[171,103],[171,275],[171,291],[172,15],[172,30],[172,124],[172,171],[172,202],[172,349],[172,456],[172,457],[173,50],[173,105],[173,218],[173,335],[173,341],[173,393],[174,27],[174,61],[174,133],[174,254],[174,263],[174,357],[175,4],[175,208],[175,274],[175,333],[175,365],[175,463],[175,498],[176,3],[176,39],[176,86],[176,103],[176,224],[176,424],[176,461],[176,476],[177,27],[177,279],[177,400],[178,125],[178,134],[178,232],[178,311],[178,345],[179,8],[179,24],[179,74],[179,192],[179,384],[179,402],[179,416],[180,169],[180,209],[180,222],[180,378],[180,390],[180,486],[181,64],[181,226],[181,238],[181,403],[181,421],[181,484],[181,485],[182,197],[182,236],[182,383],[182,476],[183,37],[183,42],[183,118],[183,125],[183,140],[183,192],[183,193],[183,200],[183,256],[184,274],[184,321],[184,441],[184,459],[185,76],[185,83],[185,123],[185,393],[185,456],[186,50],[186,62],[186,117],[186,162],[186,230],[186,379],[186,406],[186,435],[186,464],[187,29],[187,62],[187,141],[187,221],[187,222],[187,288],[187,298],[187,307],[187,336],[187,391],[188,0],[188,65],[188,79],[188,110],[188,114],[188,120],[188,237],[188,247],[188,355],[188,423],[188,467],[189,58],[189,370],[189,377],[189,422],[190,11],[190,49],[190,65],[190,235],[190,272],[190,417],[190,463],[191,33],[191,140],[191,459],[192,285],[193,0],[193,56],[193,79],[193,94],[193,114],[193,397],[193,470],[194,47],[194,49],[194,153],[194,291],[194,327],[194,390],[194,413],[195,98],[195,148],[195,219],[195,306],[195,327],[195,398],[196,8],[196,68],[196,91],[196,228],[197,38],[197,46],[197,272],[197,308],[197,331],[197,436],[198,58],[198,127],[198,199],[198,308],[198,327],[198,351],[198,367],[198,466],[198,474],[198,488],[199,5],[199,129],[199,450],[199,462],[199,483],[199,488],[199,497],[200,87],[200,263],[200,320],[200,448],[201,155],[201,299],[201,307],[201,434],[202,7],[202,229],[202,272],[202,308],[203,149],[203,189],[203,197],[203,282],[203,300],[203,312],[203,386],[203,394],[203,421],[203,441],[203,443],[203,445],[204,48],[204,126],[204,143],[204,168],[204,246],[204,251],[204,267],[204,365],[204,373],[205,16],[205,18],[205,134],[205,388],[206,43],[206,195],[206,207],[206,217],[206,220],[206,402],[206,430],[206,445],[206,478],[207,69],[207,83],[207,138],[207,226],[207,253],[207,270],[207,300],[207,345],[207,374],[207,389],[207,391],[207,394],[207,413],[207,419],[207,468],[208,47],[208,89],[208,121],[208,411],[208,413],[208,477],[209,11],[209,37],[209,120],[209,157],[209,195],[209,232],[209,309],[209,336],[209,353],[209,403],[209,479],[210,217],[210,257],[210,311],[210,362],[211,1],[211,8],[211,65],[211,124],[211,168],[211,175],[211,217],[211,422],[212,10],[212,81],[212,172],[212,186],[212,282],[213,2],[213,66],[213,213],[213,297],[213,300],[213,439],[213,479],[214,58],[214,101],[214,308],[214,421],[214,488],[215,97],[215,146],[215,223],[215,233],[215,249],[215,254],[216,67],[216,150],[216,191],[216,266],[217,73],[217,104],[217,112],[217,207],[217,254],[218,210],[218,242],[218,252],[218,433],[218,449],[219,21],[219,255],[219,257],[219,283],[219,332],[219,399],[219,415],[219,442],[220,93],[220,233],[220,240],[220,270],[220,336],[220,396],[221,8],[221,19],[221,61],[221,159],[221,186],[221,226],[221,269],[221,283],[221,350],[221,356],[221,373],[221,382],[222,39],[222,172],[222,252],[222,255],[222,272],[222,362],[222,431],[222,499],[223,115],[223,179],[223,253],[223,259],[223,400],[223,438],[224,63],[224,96],[224,132],[224,134],[224,177],[224,228],[224,338],[224,381],[225,19],[225,118],[225,137],[225,233],[225,271],[225,273],[225,283],[225,285],[225,377],[225,448],[225,449],[225,450],[226,17],[226,27],[226,57],[226,105],[226,110],[226,136],[226,199],[226,241],[226,278],[226,353],[226,355],[226,485],[227,45],[227,285],[227,298],[227,301],[228,51],[228,170],[228,182],[228,224],[228,234],[228,377],[228,473],[229,7],[229,23],[229,60],[229,226],[229,279],[229,404],[229,418],[229,460],[230,4],[230,53],[230,67],[230,74],[230,125],[230,201],[230,206],[230,216],[230,235],[231,73],[231,182],[231,401],[232,20],[232,27],[232,66],[232,226],[232,228],[232,413],[232,419],[233,42],[233,122],[233,152],[233,203],[233,232],[233,282],[233,408],[233,420],[233,466],[234,102],[234,228],[234,250],[234,295],[234,415],[234,461],[235,98],[235,280],[235,289],[235,311],[235,348],[235,361],[235,402],[235,455],[236,15],[236,34],[236,103],[236,108],[236,156],[236,275],[236,279],[236,313],[237,148],[237,329],[237,402],[237,412],[237,461],[238,20],[238,36],[238,88],[238,108],[238,206],[238,323],[238,343],[239,211],[239,244],[239,339],[239,352],[240,95],[240,150],[240,189],[240,354],[240,365],[241,147],[241,176],[241,189],[241,423],[242,63],[242,72],[242,164],[242,216],[242,219],[242,221],[242,275],[242,412],[243,140],[243,192],[243,217],[243,222],[243,344],[243,348],[243,428],[244,17],[244,200],[244,222],[244,236],[244,247],[245,102],[245,123],[245,167],[245,188],[245,318],[245,331],[245,421],[245,470],[246,147],[246,372],[246,478],[247,31],[247,192],[247,349],[247,369],[248,66],[248,203],[248,285],[248,358],[248,385],[248,487],[249,24],[249,42],[249,166],[249,279],[249,325],[249,376],[249,490],[250,108],[250,144],[250,225],[250,363],[250,364],[250,379],[250,432],[250,495],[251,112],[251,138],[251,140],[251,203],[251,440],[252,16],[252,32],[252,35],[252,143],[252,162],[252,272],[252,381],[252,400],[253,50],[253,53],[253,72],[253,181],[253,210],[253,294],[253,314],[253,400],[253,499],[254,232],[254,494],[255,95],[255,135],[255,190],[255,287],[255,314],[255,337],[255,364],[255,378],[255,390],[255,481],[255,490],[256,80],[256,197],[256,204],[256,240],[256,260],[256,274],[256,342],[256,356],[256,413],[256,449],[257,40],[257,56],[257,139],[257,343],[257,433],[258,148],[258,268],[258,450],[259,213],[259,282],[259,343],[259,380],[259,395],[259,414],[260,55],[260,58],[260,66],[260,114],[260,146],[260,160],[260,344],[261,92],[261,220],[261,273],[261,293],[261,336],[261,374],[261,426],[262,174],[262,305],[262,367],[262,496],[263,43],[263,83],[263,252],[263,276],[263,295],[263,386],[263,449],[263,459],[263,491],[263,492],[264,57],[264,144],[264,245],[264,265],[264,276],[264,446],[265,74],[265,77],[265,143],[265,284],[265,308],[265,312],[265,354],[265,386],[265,395],[265,469],[265,479],[266,68],[266,112],[266,197],[266,204],[266,248],[266,276],[266,294],[266,308],[266,363],[266,442],[266,452],[267,23],[267,78],[267,257],[267,370],[268,7],[268,23],[268,55],[268,183],[268,205],[268,227],[268,240],[268,277],[268,354],[268,469],[269,11],[269,124],[269,135],[269,160],[269,273],[269,329],[269,375],[269,387],[269,415],[270,34],[270,39],[270,48],[271,59],[271,118],[271,158],[271,172],[271,232],[271,263],[271,288],[271,445],[271,476],[272,77],[272,107],[272,285],[272,413],[272,445],[272,450],[273,117],[273,158],[273,303],[274,27],[274,56],[274,133],[274,163],[274,172],[274,174],[274,214],[274,374],[274,377],[274,454],[275,3],[275,119],[275,286],[275,320],[275,405],[275,475],[276,157],[276,267],[276,309],[276,317],[276,445],[277,75],[277,95],[277,145],[277,163],[277,175],[277,216],[277,338],[277,339],[277,409],[277,454],[278,32],[278,91],[278,141],[278,339],[278,361],[278,369],[278,400],[278,401],[278,480],[279,28],[279,52],[279,72],[279,100],[279,101],[279,194],[279,346],[279,391],[280,3],[280,99],[280,210],[280,275],[280,312],[280,404],[281,4],[281,77],[281,123],[281,139],[281,170],[281,231],[281,315],[281,326],[281,495],[282,6],[282,107],[282,113],[282,138],[282,154],[282,266],[282,301],[282,438],[283,180],[283,353],[283,459],[284,4],[284,23],[284,50],[284,95],[284,115],[284,225],[284,247],[284,305],[284,403],[285,85],[285,155],[285,191],[285,221],[285,235],[285,251],[285,350],[285,431],[286,160],[286,229],[286,237],[286,263],[286,264],[286,294],[286,371],[286,422],[287,64],[287,78],[287,105],[287,228],[287,397],[288,53],[288,185],[288,242],[288,322],[288,476],[289,6],[289,40],[289,155],[289,262],[289,414],[289,418],[289,423],[289,449],[289,468],[290,234],[290,304],[290,338],[290,389],[290,405],[290,454],[291,10],[291,44],[291,136],[291,173],[291,211],[291,290],[292,265],[292,284],[292,366],[293,94],[293,191],[293,210],[293,226],[293,302],[293,454],[294,42],[294,62],[294,256],[294,276],[294,317],[294,345],[294,453],[295,5],[295,59],[295,120],[295,164],[295,177],[295,231],[295,233],[295,260],[295,277],[295,339],[295,396],[296,150],[296,185],[296,188],[296,265],[296,361],[296,441],[297,11],[297,16],[297,41],[297,66],[297,105],[297,209],[297,219],[297,310],[297,342],[297,430],[297,432],[297,454],[297,466],[298,30],[298,70],[298,86],[298,241],[298,414],[299,19],[299,32],[299,134],[299,137],[299,281],[299,393],[299,412],[299,431],[299,478],[299,499],[300,179],[300,276],[300,303],[300,396],[300,429],[300,465],[301,376],[301,418],[302,44],[302,67],[302,78],[302,199],[302,287],[302,407],[303,8],[303,95],[303,123],[303,270],[303,402],[303,472],[303,497],[304,16],[304,41],[304,112],[304,174],[304,210],[304,219],[304,258],[304,321],[304,326],[304,494],[305,28],[305,85],[305,162],[305,355],[306,54],[306,110],[306,165],[306,199],[306,204],[306,218],[306,356],[306,369],[306,439],[306,459],[307,116],[307,180],[307,241],[307,245],[307,320],[307,328],[307,329],[307,357],[307,422],[307,484],[308,28],[308,320],[308,326],[308,353],[308,368],[308,406],[308,473],[309,297],[309,316],[309,399],[309,438],[310,216],[310,272],[310,343],[310,356],[310,413],[310,446],[310,498],[311,115],[311,126],[311,127],[311,221],[311,255],[311,356],[311,387],[311,416],[311,417],[312,136],[312,181],[312,203],[312,204],[313,237],[313,323],[313,396],[313,458],[313,468],[314,135],[314,215],[314,373],[314,375],[314,429],[314,431],[315,11],[315,145],[315,154],[315,155],[315,333],[315,466],[315,471],[315,487],[316,144],[316,334],[316,365],[317,84],[317,187],[317,231],[317,276],[317,369],[317,411],[317,440],[318,23],[318,28],[318,160],[318,355],[318,440],[318,447],[319,33],[319,239],[320,136],[320,177],[320,261],[320,390],[320,478],[321,227],[321,230],[321,315],[321,402],[321,415],[322,26],[322,36],[322,45],[322,145],[322,295],[322,385],[322,392],[322,483],[322,494],[323,57],[323,242],[323,246],[323,255],[323,289],[323,291],[323,426],[323,427],[323,471],[324,1],[324,58],[324,229],[324,297],[324,354],[324,404],[324,451],[324,477],[324,489],[325,137],[325,144],[325,252],[325,293],[325,307],[325,406],[325,422],[326,26],[326,90],[326,146],[326,225],[326,238],[326,274],[326,392],[326,393],[326,468],[327,180],[327,217],[327,286],[327,322],[327,361],[327,447],[328,128],[328,151],[328,159],[328,216],[328,452],[328,454],[328,464],[329,299],[329,406],[329,496],[330,153],[330,220],[330,371],[330,454],[331,41],[331,154],[331,165],[331,166],[331,187],[331,301],[331,361],[331,371],[331,390],[332,0],[332,24],[332,39],[332,87],[332,222],[332,308],[332,339],[332,433],[332,479],[333,147],[333,194],[333,225],[333,292],[333,408],[333,419],[333,482],[335,4],[335,175],[335,231],[335,381],[335,385],[335,442],[336,23],[336,164],[336,350],[336,436],[336,494],[337,59],[337,243],[337,424],[337,491],[338,152],[338,482],[339,43],[339,89],[339,185],[339,198],[339,296],[339,403],[339,495],[340,29],[340,239],[340,335],[341,36],[341,57],[341,490],[342,25],[342,60],[342,62],[342,105],[342,193],[342,231],[342,296],[342,342],[342,440],[342,494],[343,28],[343,72],[343,122],[343,204],[343,269],[343,374],[343,407],[343,477],[344,24],[344,132],[344,150],[344,167],[344,289],[344,331],[344,349],[344,350],[344,375],[344,395],[345,418],[345,460],[345,489],[346,88],[346,152],[346,393],[346,458],[346,478],[347,154],[347,180],[347,405],[347,490],[347,492],[348,99],[348,121],[348,163],[348,240],[348,241],[348,265],[348,271],[348,320],[348,355],[348,367],[348,474],[348,494],[349,5],[349,22],[349,75],[349,115],[349,255],[349,287],[349,299],[349,364],[349,472],[350,88],[350,102],[350,146],[350,157],[350,187],[350,286],[350,305],[350,310],[350,321],[350,323],[350,426],[351,2],[351,31],[351,39],[351,87],[351,188],[351,199],[351,218],[351,245],[351,373],[351,378],[351,457],[351,459],[351,487],[352,46],[352,78],[352,88],[352,278],[352,292],[352,332],[352,368],[352,442],[352,493],[353,103],[353,181],[353,205],[353,238],[353,264],[353,313],[353,320],[353,450],[353,496],[354,47],[354,69],[354,150],[354,218],[354,275],[355,172],[355,179],[355,216],[355,344],[355,389],[355,395],[355,450],[356,86],[356,160],[356,218],[356,350],[357,207],[357,436],[358,1],[358,142],[358,157],[358,183],[358,238],[358,266],[358,347],[358,414],[358,436],[359,32],[359,140],[359,146],[359,272],[359,273],[359,275],[359,310],[359,390],[359,429],[359,475],[359,489],[360,75],[360,236],[360,255],[360,365],[360,404],[360,458],[361,54],[361,225],[361,233],[361,277],[361,303],[361,345],[361,349],[361,380],[361,433],[361,451],[361,497],[362,20],[362,65],[362,72],[362,189],[362,422],[363,54],[363,138],[363,336],[363,440],[364,12],[364,50],[364,74],[364,118],[364,192],[364,339],[365,12],[365,46],[365,174],[365,182],[365,365],[365,430],[365,470],[366,150],[366,250],[366,299],[366,315],[366,340],[366,344],[366,351],[366,380],[367,0],[367,5],[367,17],[367,38],[367,261],[367,287],[367,399],[368,32],[368,194],[368,344],[368,354],[368,360],[368,420],[368,485],[369,17],[369,110],[369,250],[369,322],[369,428],[369,486],[370,174],[370,190],[370,449],[370,483],[371,35],[371,45],[371,181],[371,366],[371,475],[372,70],[372,136],[372,195],[372,262],[372,284],[372,317],[372,340],[372,401],[373,51],[373,111],[373,133],[373,140],[373,249],[373,278],[373,403],[374,22],[374,54],[374,103],[374,136],[374,239],[374,276],[374,345],[374,357],[375,0],[375,10],[375,49],[375,92],[375,460],[376,76],[376,159],[376,342],[376,345],[377,152],[377,159],[377,183],[377,386],[378,40],[378,67],[378,167],[378,250],[379,149],[379,159],[379,177],[380,69],[380,383],[381,173],[381,288],[381,337],[382,41],[382,129],[382,232],[382,330],[382,424],[383,25],[383,63],[383,153],[383,339],[383,359],[383,438],[383,458],[383,485],[384,134],[384,391],[384,435],[384,451],[385,38],[385,171],[385,319],[385,329],[385,365],[385,489],[386,332],[387,65],[387,101],[387,139],[387,173],[387,243],[387,471],[388,50],[388,142],[388,327],[389,13],[389,151],[389,261],[389,265],[389,293],[389,337],[389,469],[389,478],[390,87],[390,96],[390,239],[391,16],[391,39],[391,233],[391,423],[391,439],[391,488],[392,28],[392,223],[392,293],[392,314],[392,428],[392,432],[392,479],[393,8],[393,71],[393,212],[393,358],[394,47],[394,402],[394,410],[395,253],[395,268],[395,428],[395,448],[396,2],[396,77],[396,133],[396,203],[396,204],[396,212],[396,255],[396,275],[396,477],[397,86],[397,186],[397,193],[397,197],[397,213],[397,246],[397,263],[397,333],[397,398],[397,470],[397,473],[397,477],[398,122],[398,128],[398,129],[398,363],[398,388],[398,496],[399,20],[399,61],[399,121],[399,152],[399,209],[399,353],[400,12],[400,68],[400,96],[400,202],[400,230],[400,293],[400,342],[400,387],[400,392],[401,211],[401,232],[401,285],[401,296],[401,303],[401,321],[401,373],[401,497],[402,58],[402,119],[402,163],[402,176],[402,307],[402,309],[402,394],[402,475],[403,170],[403,189],[403,429],[404,0],[404,44],[404,241],[404,265],[404,315],[404,414],[404,470],[405,53],[405,106],[405,367],[405,393],[405,410],[405,433],[405,483],[406,20],[406,48],[406,125],[406,158],[406,163],[406,201],[406,279],[406,309],[407,6],[407,107],[407,175],[407,199],[407,234],[407,329],[407,444],[408,156],[408,197],[408,280],[408,299],[408,301],[408,321],[408,353],[408,406],[408,447],[409,2],[409,120],[409,146],[409,302],[409,315],[409,339],[409,367],[409,409],[409,443],[410,5],[410,84],[410,136],[410,163],[410,173],[410,299],[410,449],[411,31],[411,62],[411,184],[411,193],[411,226],[411,313],[411,429],[412,20],[412,82],[412,194],[412,231],[412,249],[412,287],[412,401],[412,405],[412,455],[413,5],[413,140],[413,170],[413,255],[413,267],[413,282],[413,390],[413,398],[413,439],[414,5],[414,29],[414,74],[414,85],[414,100],[414,179],[414,312],[414,337],[415,9],[415,39],[415,86],[415,245],[415,266],[415,312],[415,348],[415,392],[415,479],[416,104],[416,180],[416,245],[416,253],[416,361],[416,375],[416,454],[417,38],[417,323],[417,328],[417,353],[418,434],[418,478],[419,370],[421,30],[421,140],[421,189],[421,346],[421,367],[421,380],[421,464],[421,497],[422,68],[422,83],[422,104],[422,168],[422,319],[422,340],[422,366],[422,385],[422,397],[422,444],[422,447],[423,136],[423,173],[423,253],[423,278],[423,429],[424,42],[424,58],[424,122],[424,410],[425,132],[425,180],[425,187],[425,207],[425,248],[425,266],[425,353],[425,379],[426,6],[426,22],[426,198],[426,229],[426,243],[426,287],[426,332],[426,348],[426,447],[427,19],[428,304],[428,359],[428,445],[428,478],[428,479],[429,76],[429,96],[429,162],[429,278],[430,247],[430,307],[430,320],[430,350],[430,360],[430,471],[431,10],[431,15],[431,94],[431,141],[431,197],[431,256],[431,300],[431,371],[431,432],[431,434],[431,499],[432,69],[432,146],[432,158],[432,240],[432,242],[432,257],[433,26],[433,79],[433,371],[433,374],[433,458],[433,468],[434,109],[434,186],[434,203],[434,204],[435,92],[435,162],[435,494],[436,12],[436,157],[436,190],[436,253],[436,311],[436,394],[436,417],[437,4],[437,76],[437,235],[437,251],[437,404],[438,52],[438,163],[439,17],[439,37],[439,108],[439,113],[439,193],[439,248],[439,253],[439,256],[439,271],[439,330],[440,79],[440,188],[440,216],[440,281],[440,455],[440,478],[441,6],[441,133],[441,372],[441,387],[441,480],[441,498],[442,133],[442,182],[442,239],[442,376],[442,424],[442,492],[443,161],[443,192],[443,476],[444,161],[444,207],[444,264],[445,44],[445,95],[445,148],[445,203],[445,256],[445,329],[446,120],[446,133],[446,147],[446,209],[446,215],[446,234],[446,259],[446,335],[447,271],[447,445],[448,126],[448,230],[448,268],[448,311],[448,364],[448,393],[448,439],[448,453],[448,492],[449,126],[449,137],[449,214],[449,250],[449,266],[449,334],[449,371],[449,390],[449,454],[450,61],[450,193],[450,380],[450,423],[450,454],[450,456],[451,154],[451,184],[451,227],[451,274],[451,357],[451,394],[451,434],[451,474],[451,486],[452,32],[452,48],[452,107],[452,183],[452,187],[452,231],[452,382],[452,401],[452,479],[452,496],[452,499],[453,32],[453,92],[453,107],[453,283],[453,330],[453,413],[454,23],[454,28],[454,132],[454,282],[454,477],[454,489],[455,11],[455,106],[455,368],[455,455],[456,4],[456,45],[456,165],[456,351],[456,458],[457,99],[457,103],[457,176],[457,209],[457,281],[457,293],[457,330],[457,419],[457,453],[458,43],[458,47],[458,139],[458,243],[458,351],[458,418],[458,478],[459,8],[459,128],[459,197],[459,215],[459,330],[459,396],[459,422],[460,224],[460,305],[460,399],[460,405],[460,438],[461,40],[461,322],[462,15],[462,74],[462,492],[462,495],[463,46],[463,98],[463,187],[463,220],[463,259],[463,292],[463,330],[463,371],[463,399],[463,418],[464,32],[464,139],[464,288],[464,337],[464,462],[464,496],[465,195],[465,356],[465,404],[465,416],[465,483],[466,26],[466,58],[466,261],[466,272],[466,313],[466,444],[466,460],[467,6],[467,60],[467,153],[467,156],[467,285],[467,398],[467,429],[467,477],[468,3],[468,94],[468,229],[468,239],[468,490],[469,7],[469,177],[469,234],[469,254],[469,364],[469,388],[470,38],[470,122],[470,221],[470,292],[470,348],[470,496],[471,37],[471,129],[471,176],[471,377],[471,393],[471,443],[472,5],[472,261],[472,272],[472,329],[472,363],[472,498],[473,100],[473,142],[473,232],[473,305],[473,316],[473,342],[473,352],[473,414],[473,423],[473,436],[473,476],[474,49],[474,171],[474,322],[474,454],[475,0],[475,31],[475,90],[475,114],[475,187],[475,193],[475,289],[475,392],[475,395],[475,415],[475,466],[476,209],[476,352],[476,408],[476,453],[477,24],[477,74],[477,109],[477,150],[477,163],[477,173],[477,189],[477,425],[478,5],[478,37],[478,248],[478,292],[478,350],[478,422],[479,45],[479,339],[479,375],[479,376],[479,401],[479,418],[479,499],[480,66],[480,171],[480,277],[480,296],[480,340],[480,441],[480,462],[481,83],[481,118],[481,133],[481,178],[481,184],[481,209],[481,226],[482,68],[482,137],[482,176],[482,201],[482,468],[482,499],[483,3],[483,47],[483,95],[483,173],[483,186],[483,231],[483,388],[484,148],[484,320],[484,343],[484,462],[484,469],[484,490],[485,13],[485,123],[485,126],[485,134],[485,323],[486,23],[486,370],[486,391],[486,424],[487,78],[487,83],[487,159],[487,223],[487,234],[487,338],[487,424],[487,432],[488,29],[488,63],[488,224],[488,393],[489,26],[489,32],[489,41],[489,152],[489,158],[489,180],[489,183],[489,190],[489,239],[489,382],[489,410],[489,412],[489,419],[490,147],[490,168],[490,251],[490,413],[490,479],[491,102],[491,161],[491,468],[492,33],[492,70],[492,100],[492,275],[492,279],[492,417],[492,455],[493,73],[493,259],[493,295],[493,301],[493,421],[493,474],[494,47],[494,316],[494,394],[494,398],[495,9],[495,97],[495,152],[495,264],[495,274],[495,322],[495,324],[495,335],[495,414],[496,28],[496,74],[496,137],[496,183],[496,189],[496,209],[496,334],[497,9],[497,156],[497,177],[497,339],[497,354],[498,160],[498,420],[498,454],[499,57],[499,81],[499,90],[499,255],[499,282],[499,475]]
mtrix=[]
s=Solution()
print(s.orderOfLargestPlusSign(10, mtrix))

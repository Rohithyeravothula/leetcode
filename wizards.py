def meet(wizards):
    # wizards=[]
    # for i in wizards_n:
    #     wizards.append(map(int, i.split()))
    l = len(wizards)
    wizmap = {index: conn for index, conn in enumerate(wizards)}
    meet.min_cost = float("inf")
    min_path = None
    def dfs(path, path_cost, seen, wizmap, target):
        if path[-1] == target:
            return path_cost, path
        elif path_cost > meet.min_path:
            return float("inf"), path
        min_cost = float("inf")
        min_path = None
        for child in wizmap[path[-1]]:
            cost = (child - path[-1])**2
            if child not in seen:
                seen.add(path[-1])
                cur_cost, cur_path = dfs(path+[child], path_cost + cost, seen, wizmap, target)
                if cur_cost < min_cost:
                    min_cost = cur_cost
                    min_path = cur_path
                seen.remove(path[-1])
        return min_cost, min_path

    
    for child in wizmap[0]:
        cur_cost, cur_path = dfs([0, child], 0, {0, child}, wizmap, l-1)
        if cur_cost < meet.min_cost:
            meet.min_cost = cur_cost
            min_path = cur_path
    print(min_path)

wizards = [[1,2,3],[8, 6, 4],[7, 8, 3],[8, 1],[6],[8, 7],[9, 4],[4, 6],[1],[1, 4]]
meet(wizards)

graph={'Garden East':set(['Lasbella','Gurumandir','Soldier Bazar']),
       'Lasbella':set(['Nazimabad']),
       'Gurumandir':set(['Liaqatabad']),
       'Soldier Bazar':set(['Numaish','Gurumandir']),
       'Nazimabad':set(['KDA']),
       'Liaqatabad':set(['Karimabad']),
       'Numaish':set(['Gurumandir','Kashmir road']),
       'KDA':set(['School']),
       'Karimabad':set(['Ziauddin']),
       'Ziauddin':set(['School']),
       'Kashmir road':set(['Gurumandir']),
       'School':set(['KDA','Karimabad']),
       'Buffer Zone':set(['Nazimabad','Water Pump']),
       'Water Pump':set(['Ayesha Manzil']),
       'Ayesha Manzil':set(['Karimabad']),
       'Al noor':set(['Sakhi Hassan','Water Pump']),
       'Sakhi Hassan':set(['KDA'])
       }
def dfs_path_finding(graph,source,destination):
    vertexs=[(source,[source])]
    while vertexs:
        (vertex,path)=vertexs.pop()
        for next in graph[vertex]-set(path):
            if next==destination:
                yield path+[next]
            else:
                vertexs.append((next,path+[next]))
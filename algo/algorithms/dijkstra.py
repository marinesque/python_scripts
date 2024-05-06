 D = ((0, 3, 1, 3, 0, 0),
      (3, 0, 4, 0, 0, 0),
      (1, 4, 0, 0, 7, 5),
      (3, 0, 0, 0, 0, 2),
      (0, 0, 7, 0, 0, 4),
      (0, 0, 5, 2, 4, 0))

 N = len(D)
 T = [math.inf]*N

 v = 0
 S = {v}
 T[v] = 0

 while v != -1:
     for j in get_link_v(v, D):
         if j not in S:
             w = T[v] + D[v][j]
             if w < T[j]:
                 T[j] = w
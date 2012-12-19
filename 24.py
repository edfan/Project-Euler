def permutation():
    permutations = []
    for a in range(0, 10):
        chosen = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        chosen.remove(a)
        for b in chosen:
            chosen = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            chosen.remove(a)
            chosen.remove(b)
            for c in chosen:
                chosen = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                chosen.remove(a)
                chosen.remove(b)
                chosen.remove(c)
                for d in chosen:
                    chosen = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                    chosen.remove(a)
                    chosen.remove(b)
                    chosen.remove(c)
                    chosen.remove(d)
                    for e in chosen:
                        chosen = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                        chosen.remove(a)
                        chosen.remove(b)
                        chosen.remove(c)
                        chosen.remove(d)
                        chosen.remove(e)
                        for f in chosen:
                            chosen = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                            chosen.remove(a)
                            chosen.remove(b)
                            chosen.remove(c)
                            chosen.remove(d)
                            chosen.remove(e)
                            chosen.remove(f)
                            for g in chosen:
                                chosen = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                                chosen.remove(a)
                                chosen.remove(b)
                                chosen.remove(c)
                                chosen.remove(d)
                                chosen.remove(e)
                                chosen.remove(f)
                                chosen.remove(g)
                                for h in chosen:
                                    chosen = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                                    chosen.remove(a)
                                    chosen.remove(b)
                                    chosen.remove(c)
                                    chosen.remove(d)
                                    chosen.remove(e)
                                    chosen.remove(f)
                                    chosen.remove(g)
                                    chosen.remove(h)
                                    for i in chosen:
                                        chosen = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                                        chosen.remove(a)
                                        chosen.remove(b)
                                        chosen.remove(c)
                                        chosen.remove(d)
                                        chosen.remove(e)
                                        chosen.remove(f)
                                        chosen.remove(g)
                                        chosen.remove(h)
                                        chosen.remove(i)
                                        for j in chosen:
                                            currentstring = str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(g) + str(h) + str(i) + str(j)
                                            permutations.append(int(currentstring))
    permutations.sort()
    return permutations

permlist = permutation()
print(permlist[999999])

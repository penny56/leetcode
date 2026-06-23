class LRUCache:

    def __init__(self, capacity: int):
        # dic = {key, [value, time]}
        self.dic = {}

        # 每个 get 就是一次使用，clock + 1
        self.clock = 0

        # 是否已满
        self.capacity = capacity

    '''
    get时，更新 time，表示最近使用了
    '''
    def get(self, key: int) -> int:

        self.clock += 1
        
        # 如果不在，返回 -1
        if key not in self.dic: return -1

        # 更新 time
        self.dic[key] = [self.dic[key][0], self.clock]

        # 返回 value
        return self.dic[key][0]


    '''
    put时，看dic，如果已存在，更新 value 与 time
                  不存在，看 capacity，如果 > 0，则插入 key-value
                                      否则，del一个 max(click - time)
    '''
    def put(self, key: int, value: int) -> None:

        # 这里其实可以不 click ++ ，但是为了防止一直put，大家都在一个clock
        self.clock += 1       
        
        if key in self.dic:
            # 若已存在
            self.dic[key] = [value, self.clock]
        
        else:
            # 若不存在
            if self.capacity > 0:
                # 若有空间
                self.dic[key] = [value, self.clock]
                self.capacity -= 1
            else:
                # 没空间，要踢人了,踢time最小的，表示最久没被get
                longestKey = min(self.dic, key = lambda k : self.dic[k][1])
                del self.dic[longestKey]

                # 加新，并把 time 设置的 self.clock 认为是最新
                self.dic[key] = [value, self.clock]

        return
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

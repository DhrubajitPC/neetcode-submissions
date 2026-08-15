class TimeMap:

    def __init__(self):
        self.hash = {}    

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hash:
            self.hash[key] = {}
        self.hash[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key in self.hash:
            res_hash = self.hash[key]
            if timestamp not in res_hash:
                timestamps = list(res_hash.keys())
                l, r = 0, len(timestamps) - 1
                prev = 0
                while l <= r:
                    m = (l + r) // 2
                    if timestamps[m] > timestamp:
                        r = m - 1
                    else:
                        prev = timestamps[m]
                        l = m + 1

                return res_hash[prev] if prev in res_hash else ""
            else:
                return res_hash[timestamp]
                

        return ""

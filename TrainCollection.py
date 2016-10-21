from prettytable import PrettyTable

class TrainCollection(object):
    header = " train station time duration first second softsleep hardsleep hardseat".split()

    def __init__(self,rows):
        self.rows = rows

    def _get_duration(self,row):
        """
        获取车次运行时间
        """
        duration = row.get("lishi").replace(":","h")+"m"
        if duration.startswith("00"):
            duration = duration[3:]
        if duration.startswith("0"):
            duration  = duration[1:]
        return duration

    def colored(self,color,text):
        table= {
            "red":"\033[91m",
            "green":"\033[92m",
            "nc":"\033[0m"
            }
        cv = table.get(color)
        nc = table.get("nc")
        return "".join([cv,text,nc])

    @property
    def trains(self):
        for row in self.rows:
            train = [
                row["station_train_code"],
                "\n".join([row["start_station_name"],row["end_station_name"]]),
                "\n".join([row["start_time"],row["arrive_time"]]),
                self._get_duration(row),
                row["zy_num"],
                row["ze_num"],
                row["rw_num"],
                row["yw_num"],
                row["yz_num"]
                ]
            yield train

    

    def pretty_print(self):
        pt = PrettyTable()
        pt._set_field_names(self.header)
        for train in self.trains:
            pt.add_row(train)
        print(pt)
        
        
    

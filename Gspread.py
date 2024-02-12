import gspread

class Gspread:
    def __init__(self, auth_file_path = None):
        print(gspread.__version__)
        if auth_file_path != None:
            self.gc = gspread.service_account(auth_file_path)
        else:
            self.gc = gspread.service_account() # default: ~/.config/gspread/service_account.json
    
    # worksheet
    def open_worksheet(self, name:str):
        self.sh = self.gc.open(name)
        self.sheets_list = self.sh.worksheets() # list up all the sheets' titles
        print(f"Sheets list: {self.sheets_list}")
    
    # sheet
    def select_sheet(self, *args):
        
        # print(type, val)
        if type(args[0]) == str:
            self.worksheet = self.sh.worksheet(args[0])
            print(f"Selected sheet name: {args[0]}")
        elif type(args[0]) == int:
            self.worksheet = self.sh.get_worksheet(args[0])
            print(f"Selected sheet index: {args[0]}")
        else:
            raise ValueError
    
    def list_sheets(self):
        print(self.sheets_list)
    
    def create_new_sheet(self, name:str, rows:int, cols:int):
        self.worksheet = self.sh.add_worksheet(title = name, rows = rows, cols = cols)
        self.sheets_list = self.sh.worksheets()
        print(f"Successfully created: {name}")
        
    def delete_sheet(self, name:str):
        self.sh.del_worksheet(self.select_sheet(name = name))
        self.sheets_list = self.sh.worksheets()
        print(f"Successfully deleted: {name}")
    
    # cell
    
    def select_by_cell(self, *args):
        if type(args[0]) == str:
            return self.worksheet.cell(args[0]).value # e.g. '18.26'
        elif type(args[0]) == int:
            return self.worksheet.cell(args[0], args[1]).value
        else:
            raise ValueError
                
    def select_by_range(self, range:str):
        return self.worksheet.get(range) # e.g. 'D6:D8' => [['18.26'], ['12.07], ['14.22']]
    
    def select_by_row_or_col(self, row_or_col:str, idx:int):
        assert row_or_col in ['row', 'col'], 'row or col'
        if row_or_col == 'row':
            return self.worksheet.row_values(idx)
        else:
            return self.worksheet.col_values(idx)
        
    def update_by_cell(self, *args):
        self.worksheet.update_cell(args[0], args[1], args[2]) # e.g. 6,4,val
    
    def update_by_range(self, *args): # e.g. 'A1:B2',[[val, val], [val,val]]
        # print(args)
        range = args[0]
        vals = args[1]
        
        self.worksheet.update(range, vals)
    
    def delete_by_range(self, range:list): # e.g. ["A1:B1", "C2:E2"]
        self.worksheet.batch_clear(range)
    
    def locate(self, start_row_idx, start_col_idx, by):
        
        row = start_row_idx
        col = start_col_idx
        
        while self.select_by_cell(row, col) != None:
            if by == 'row':
                row += 1
            else:
                col += 1
                
        return row, col
    

class CustomLogger(Gspread):
    def __init__(self, model_name, open_closed, batch_size, lr, n_steps = "", step_size = "", standard = "", loss = ""):
        super().__init__()
        self.open_worksheet("Energy_based_TTA")
        self.select_sheet("TENT vs EBM")
        row_idx, _ = self.locate(50,2, by = 'row')
        self.update_by_range(f"B{row_idx}:H{row_idx}", [[f"{model_name} ({open_closed}, batch = {batch_size})", f"{lr}", "", f"{n_steps}", f"{step_size}", f"{standard}", f"{loss}"]])
        self.cell_id = [row_idx, 9]
        
    def log_errate(self, err:float):
        self.update_by_cell(self.cell_id[0], self.cell_id[1], f"{err*100:2}")
        self.cell_id[1] += 1
        
    def log_ertype(self):
        pass
        
    
    
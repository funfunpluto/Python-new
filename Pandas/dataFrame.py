
#play with df 

        df = readCsv(izyfile, ['Key','Seq'])
        #print(df.tail())
        #print(df.info())
        #print(df['Key'].unique())
        #print(df['Key'].describe())
        key = df.groupby('Key')
        print(key.sum())

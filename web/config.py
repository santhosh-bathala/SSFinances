import os
# SECRET_KEY = '$2b$12$F.jh9Uv1UDBC/sLGIa2UPudjqHdD8rp/kQVG1WGnsusJmT15TRIce'
SECRET_KEY = os.getenv('SECRET_KEY')
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://u485156025_ssfinances:Anvi123xyz@srv1642.hstgr.io/u485156025_ssfinances'
SQLALCHEMY_DATABASE_URI = 'postgresql://' + os.getenv('USERNAME') +':AVNS_syxUV20eOwjYfAOOe7N@pg-c217c2b-santosh-ssfinaces.k.aivencloud.com:17047/defaultdb?sslmode=require'





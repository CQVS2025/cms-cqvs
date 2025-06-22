import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import json

df_scans = pd.DataFrame(json.loads('''[
  {
    "Unnamed: 0": NaN,
    "Aging": "1 hour ago",
    "Created": "2025-06-22 13:56:05",
    "Customer": "BORAL - QLD",
    "Site": "Benowa",
    "Vehicle Name": "40099",
    "Genie": "Coletek 088",
    "RFID": "060388046d1719",
    "Last Tank Level (m)": -1,
    "Wash Time": 180,
    "Version": "2.1.2.89",
    "Status": "Success"
  },
  {
    "Unnamed: 0": NaN,
    "Aging": "1 day ago",
    "Created": "2025-06-21 12:36:55",
    "Customer": "BORAL - QLD",
    "Site": "Redbank",
    "Vehicle Name": "45306",
    "Genie": "Coletek3.007",
    "RFID": "6.04E+12",
    "Last Tank Level (m)": -1,
    "Wash Time": 120,
    "Version": "2.1.2.86",
    "Status": "Success"
  },
  {
    "Unnamed: 0": NaN,
    "Aging": "1 day ago",
    "Created": "2025-06-21 11:39:57",
    "Customer": "BORAL - QLD",
    "Site": "Redbank",
    "Vehicle Name": "40848",
    "Genie": "Coletek3.007",
    "RFID": "06038804655d57",
    "Last Tank Level (m)": -1,
    "Wash Time": 120,
    "Version": "2.1.2.86",
    "Status": "Success"
  },
  {
    "Unnamed: 0": NaN,
    "Aging": "1 day ago",
    "Created": "2025-06-21 10:58:37",
    "Customer": "BORAL - QLD",
    "Site": "Geebung",
    "Vehicle Name": "289",
    "Genie": "Coletek 064",
    "RFID": "0603880423aa62",
    "Last Tank Level (m)": -1,
    "Wash Time": 60,
    "Version": "2.1.2.71",
    "Status": "Success"
  },
  {
    "Unnamed: 0": NaN,
    "Aging": "1 day ago",
    "Created": "2025-06-21 10:56:48",
    "Customer": "BORAL - QLD",
    "Site": "Geebung",
    "Vehicle Name": "289",
    "Genie": "Coletek 064",
    "RFID": "0603880423aa62",
    "Last Tank Level (m)": -1,
    "Wash Time": 60,
    "Version": "2.1.2.71",
    "Status": "Success"
  }
]'''))
df_vehicles = pd.DataFrame(json.loads('''[
  {
    "Unnamed: 0": NaN,
    "Customer": "BORAL - QLD",
    "Site": "Benowa",
    "Vehicle Name": "40099",
    "Vehicle RFID": "060388046d1719",
    "Wash Time": "180 Secs",
    "Washes Day/Week": "1/6",
    "Protocol": 12,
    "Last Scan": "2025-06-22 13:56:05",
    "Status": "Active",
    "Actions": NaN
  },
  {
    "Unnamed: 0": NaN,
    "Customer": "BORAL - QLD",
    "Site": "Redbank",
    "Vehicle Name": "45306",
    "Vehicle RFID": "6.04E+12",
    "Wash Time": "120 Secs",
    "Washes Day/Week": "1/6",
    "Protocol": 12,
    "Last Scan": "2025-06-21 12:36:55",
    "Status": "Active",
    "Actions": NaN
  },
  {
    "Unnamed: 0": NaN,
    "Customer": "BORAL - QLD",
    "Site": "Redbank",
    "Vehicle Name": "40848",
    "Vehicle RFID": "06038804655d57",
    "Wash Time": "120 Secs",
    "Washes Day/Week": "1/6",
    "Protocol": 12,
    "Last Scan": "2025-06-21 11:39:57",
    "Status": "Active",
    "Actions": NaN
  },
  {
    "Unnamed: 0": NaN,
    "Customer": "BORAL - QLD",
    "Site": "Geebung",
    "Vehicle Name": "289",
    "Vehicle RFID": "0603880423aa62",
    "Wash Time": "60 Secs",
    "Washes Day/Week": "2/12",
    "Protocol": 24,
    "Last Scan": "2025-06-21 10:58:37",
    "Status": "Active",
    "Actions": NaN
  },
  {
    "Unnamed: 0": NaN,
    "Customer": "BORAL - QLD",
    "Site": "Capalaba",
    "Vehicle Name": "Spare 1",
    "Vehicle RFID": "0603880490052a",
    "Wash Time": "90 Secs",
    "Washes Day/Week": "2/4",
    "Protocol": 12,
    "Last Scan": "2025-06-21 10:18:36",
    "Status": "Active",
    "Actions": NaN
  }
]'''))
df_refills = pd.DataFrame(json.loads('''[
  {
    "Unnamed: 0": NaN,
    "Ref": "E04695",
    "Customer": "BORAL - QLD",
    "Site": "Geebung",
    "Area Manager (Users Name)": "Jonny Harper",
    "Date": "Mon, 4 Aug, 2025",
    "Invoice No": "---",
    "Product": "ELORA CONCRETE SAFE REMOVER - ECSR ($3.85)",
    "Start (l)": 0,
    "New Total (l)": 700,
    "Delivered (l)": 700,
    "Rate ($)": "$3.85",
    "Total (Ex.GST)": "$2,695.00",
    "PO": "---",
    "Status": "Scheduled",
    "Actions": NaN
  },
  {
    "Unnamed: 0": NaN,
    "Ref": "E04643",
    "Customer": "BORAL - QLD",
    "Site": "Benowa",
    "Area Manager (Users Name)": "Jonny Harper",
    "Date": "Thu, 31 Jul, 2025",
    "Invoice No": "---",
    "Product": "ELORA CONCRETE SAFE REMOVER - ECSR ($3.85)",
    "Start (l)": 0,
    "New Total (l)": 800,
    "Delivered (l)": 800,
    "Rate ($)": "$3.85",
    "Total (Ex.GST)": "$3,080.00",
    "PO": "---",
    "Status": "Scheduled",
    "Actions": NaN
  },
  {
    "Unnamed: 0": NaN,
    "Ref": "E04621",
    "Customer": "BORAL - QLD",
    "Site": "Narangba",
    "Area Manager (Users Name)": "Jonny Harper",
    "Date": "Wed, 23 Jul, 2025",
    "Invoice No": "---",
    "Product": "ELORA CONCRETE SAFE REMOVER - ECSR ($3.85)",
    "Start (l)": 0,
    "New Total (l)": 1000,
    "Delivered (l)": 1000,
    "Rate ($)": "$3.85",
    "Total (Ex.GST)": "$3,850.00",
    "PO": "---",
    "Status": "Scheduled",
    "Actions": NaN
  },
  {
    "Unnamed: 0": NaN,
    "Ref": "E04708",
    "Customer": "BORAL - QLD",
    "Site": "Labrador",
    "Area Manager (Users Name)": "Jonny Harper",
    "Date": "Fri, 18 Jul, 2025",
    "Invoice No": "---",
    "Product": "ELORA CONCRETE SAFE REMOVER - ECSR ($3.85)",
    "Start (l)": 0,
    "New Total (l)": 440,
    "Delivered (l)": 440,
    "Rate ($)": "$3.85",
    "Total (Ex.GST)": "$1,694.00",
    "PO": "---",
    "Status": "Scheduled",
    "Actions": NaN
  },
  {
    "Unnamed: 0": NaN,
    "Ref": "E04629",
    "Customer": "BORAL - QLD",
    "Site": "Everton Park",
    "Area Manager (Users Name)": "Jonny Harper",
    "Date": "Wed, 16 Jul, 2025",
    "Invoice No": "---",
    "Product": "ELORA CONCRETE SAFE REMOVER - ECSR ($3.85)",
    "Start (l)": 0,
    "New Total (l)": 700,
    "Delivered (l)": 700,
    "Rate ($)": "$3.85",
    "Total (Ex.GST)": "$2,695.00",
    "PO": "---",
    "Status": "Scheduled",
    "Actions": NaN
  }
]'''))
df_clients = pd.DataFrame(json.loads('''[
  {
    "Company": "Wayne Thorneycroft & Andrew Gibbons - Gold Coast",
    "Site": NaN,
    "Location": NaN,
    "Phone Number": "Andrew: 0478 271 014 Wayne: 0401 896 371",
    "Status": NaN,
    "Notes": NaN
  },
  {
    "Company": "BORAL \u2013 QLD",
    "Site": "Benowa",
    "Location": "20 Racecourse Dr, Bundall QLD 4217",
    "Phone Number": "0448 688 798",
    "Status": "Active",
    "Notes": "21 / 01 \u2013 Up to date. 29 / 08 / 24 \u2013 The system was turned off and isolated due to spraying over a worker, now all fixed. All Systems Go. 02 / 06 / 24 \u2013 Need site update?? Worst Batcher on Earth."
  },
  {
    "Company": "BORAL \u2013 QLD",
    "Site": "Burleigh",
    "Location": "18 Rudman Parade, Burleigh Heads QLD 4220",
    "Phone Number": NaN,
    "Status": "Active",
    "Notes": "05 / 08 / 24 \u2013 No Truck Wash computer; the system is up to date. Roof struts are installed correctly. 02 / 06 / 24 \u2013 did roof struts installed correctly? 13 / 05 / 24 \u2013 need approval for May delivery."
  },
  {
    "Company": "BORAL \u2013 QLD",
    "Site": "Labrador",
    "Location": "243 Brisbane Rd, Biggera Waters QLD 4214",
    "Phone Number": "Geoff: 0418 787 587",
    "Status": "Active",
    "Notes": "21 / 01 \u2013 Up to date \u2013 needs upgrade. Geoff Batcher \u2013 0418 787 587 24 / 07 \u2013 new light and siren, create sun cover, acid box ventilation. 02 / 06 \u2013 Up to date. 13 / 05 \u2013 Need airline fix and 5 \u00d7 scan cards."
  },
  {
    "Company": "BORAL \u2013 QLD",
    "Site": "Southport",
    "Location": "47 Bailey Cres, Southport QLD 4215",
    "Phone Number": NaN,
    "Status": "Active",
    "Notes": "21 / 01 \u2013 Ready for a quote \u2013 to speak to Andrew. 02 / 06 Blair to investigate full system installation."
  }
]'''))
df_contacts = pd.DataFrame(json.loads('''[
  {
    "Name": "Untitled 20d6ed160c54803abf67f508e8c0d930",
    "Phones": "",
    "Emails": "",
    "Notes": "# Untitled"
  },
  {
    "Name": "Wayne Thorneycroft & Andrew Gibbons",
    "Phones": "0401 896 371, 0478 271 014",
    "Emails": "",
    "Notes": "# Wayne Thorneycroft & Andrew Gibbons - Gold Coast  Phone Number: Andrew: 0478 271 014 Wayne: 0401 896 371"
  },
  {
    "Name": "Untitled 20d6ed160c548059ba6ad08cc8302700",
    "Phones": "",
    "Emails": "",
    "Notes": "# Untitled"
  },
  {
    "Name": "Jason Baker",
    "Phones": "0401 896 964",
    "Emails": "",
    "Notes": "# Jason Baker - Brisbane South  Phone Number: Jason: 0401 896 964"
  },
  {
    "Name": "Andrew Tanovic",
    "Phones": "",
    "Emails": "",
    "Notes": "# Andrew Tanovic - Wagners"
  }
]'''))

st.set_page_config(page_title='CQVS CMS', layout='wide')
page = st.sidebar.radio('Go to', ['Dashboard', 'Vehicles', 'Scans', 'Refills', 'Clients', 'Contacts'])

if page == 'Dashboard':
    st.title('📊 Dashboard')
    df_scans['Created'] = pd.to_datetime(df_scans['Created'], errors='coerce')
    recent = df_scans[df_scans['Created'] > (datetime.now() - timedelta(days=7))]
    st.metric('Washes (last 7 days)', len(recent))
    if not recent.empty:
        st.bar_chart(recent['Vehicle Name'].value_counts())

elif page == 'Vehicles':
    st.title('🚛 Vehicles')
    st.dataframe(df_vehicles)

elif page == 'Scans':
    st.title('🧼 Wash Scans')
    st.dataframe(df_scans)

elif page == 'Refills':
    st.title('🧪 Refills')
    st.dataframe(df_refills)

elif page == 'Clients':
    st.title('🏢 Clients')
    st.dataframe(df_clients)

elif page == 'Contacts':
    st.title('📇 Contacts')
    st.dataframe(df_contacts)

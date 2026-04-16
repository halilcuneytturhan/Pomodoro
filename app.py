
import time
import streamlit as st

# --- SAYFA TASARIMI (CSS ENJEKSİYONU) ---
st.markdown("""
<style>
    /* 1. Kutu Üstündeki Yazılar (Dakika giriniz vb.) */
    [data-testid="stWidgetLabel"] p {
        font-size: 24px !important;
        font-family: 'New Times Roman', Courier, monospace !important;
        color: #fcfcfc !important; /* Neon Yeşil */
        font-weight: bold !important;
    }

    /* 2. Kutunun İçindeki Sayılar */
    input[type="number"] {
        font-size: 22px !important;
        font-family: 'Courier New', Courier, monospace !important;
        color: white !important;
        font-weight: bold !important;
    }
</style>
""", unsafe_allow_html=True)
# ----------------------------------------

if "mod" not in st.session_state:
    st.session_state.mod = "Ders"

if "oturum_sayisi" not in st.session_state:
    st.session_state.oturum_sayisi = 0
    
if "calisiyor" not in st.session_state:
    st.session_state.calisiyor = False # Başlangıçta sayaç duruyor
    
if "kalan_saniye" not in st.session_state:
    st.session_state.kalan_saniye = 0 # Başlangıçta süremiz 0



sayac_alani = st.container()
st.write("----")
dakika = st.number_input("Dakika giriniz",min_value=1,step=1)


buton_alani = st.container()


with buton_alani:
    col1,col2,col3 = st.columns(3)
    col4,col5,col6 = st.columns(3)



    if(col1.button("Başlat")):
        st.session_state.mod = "Ders"
        st.session_state.calisiyor = True
        st.session_state.kalan_saniye = (dakika * 60)

    if(col4.button("Başlangıç (20 dk)")):
        st.session_state.mod = "Ders"
        st.session_state.kalan_saniye = 20 * 60
        st.session_state.calisiyor = True

    if(col5.button("İdeal (25 dk)")):
        st.session_state.mod = "Ders"
        st.session_state.kalan_saniye = 25 * 60
        st.session_state.calisiyor = True    
        
    if(col6.button("MOLA")):
        st.session_state.mola_menusu = not st.session_state.mola_menusu


    if('mola_menusu' not in st.session_state):
        st.session_state.mola_menusu = 0
        

    def oturum():
        st.write(f"Şuan ki oturum sayısı =  {st.session_state.oturum_sayisi}")
        
        if(st.button("15 DK")):
            st.session_state.mod = "Mola"
            st.session_state.mola_menusu = False
            st.write("15 DK mola basladı")
            st.session_state.kalan_saniye = 15 * 60
            st.session_state.calisiyor = True
            
        if(st.button("30 DK")):
            st.session_state.mola_menusu = 0
            st.session_state.mod = "Mola"
            st.session_state.kalan_saniye = 30 * 60
            st.session_state.calisiyor = True
            
            st.write("30 DK mola basladı")
                    

    if(st.session_state.mola_menusu == True):
        oturum()
    
    if(col2.button("Duraklat")):
        st.session_state.calisiyor = False
        
    if(col3.button("Sıfırla")):
        st.session_state.calisiyor = False
        st.session_state.kalan_saniye = 0
        


# Saniyede bir SADECE bu fonksiyonun içini çalıştırır! Sayfa titremez.
@st.fragment(run_every=1) 
def motor_ve_ekran():
    
    # 1. MOTOR KISMI (Saniyeyi azalt)
    if st.session_state.calisiyor == True and st.session_state.kalan_saniye > 0:
        st.session_state.kalan_saniye -= 1

    # 2. MATEMATİK KISMI
    dk = st.session_state.kalan_saniye // 60
    sn = st.session_state.kalan_saniye % 60

    # 3. TASARIM VE RENK KISMI
    if st.session_state.mod == "Mola":
        ust_yazi = "MOLANIN BİTMESİNE"
        tema_rengi = "#00E5FF"
    else:
        ust_yazi = "ODAKLANMA VAKTİ"
        tema_rengi = "#39FF14"

    # Ekrana bas (sayac.markdown yerine direkt st.markdown kullanıyoruz)
    st.markdown(f"""
    <div style='text-align: center; margin-bottom: 10px;'>
        <h3 style='color: {tema_rengi}; font-family: New Times Roman; letter-spacing: 2px;'>{ust_yazi}</h3>
    </div>
    <div style='background-color: #1e1e1e; border-radius: 30px; text-align: center; border: 4px solid {tema_rengi}; box-shadow: 0px 0px 25px {tema_rengi}55; padding: 30px;'>
      <h1 style='color: {tema_rengi}; font-size: 90px; font-family: New Times Roman; margin:0;'>{dk:02d}:{sn:02d}</h1>
    </div>
    """, unsafe_allow_html=True)

    # 4. SÜRE BİTME KONTROLÜ
    if st.session_state.calisiyor == True and st.session_state.kalan_saniye == 0:
        st.session_state.calisiyor = False
        st.session_state.oturum_sayisi += 1
        st.success(f"Oturum Bitti! Toplam: {st.session_state.oturum_sayisi}")

# Kalkanlı fonksiyonu sayfanın sonunda çağırıyoruz ki ekranda görünsün
with sayac_alani:
    motor_ve_ekran()










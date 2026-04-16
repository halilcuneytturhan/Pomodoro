
import time
import streamlit as st
#pushlandi.


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
dakika = st.number_input("Dakika giriniz veya butonlardan dk seçiniz.",min_value=1,step=1)


buton_alani = st.container()


with buton_alani:
    col1,col2,col3 = st.columns(3)
    st.write("\n\n")
    col4,col5,col6,col7= st.columns(4)
    st.write("\n\n")
    col8,col9 = st.columns(2)
    st.write("\n\n")
    col10,col11 = st.columns(2)
    


    if(col1.button("Başlat",use_container_width=True)):
        st.session_state.mod = "Ders"
        st.session_state.calisiyor = True
        st.session_state.kalan_saniye = (dakika * 60)

    if(col4.button("Başlangıç (20 dk)",use_container_width=True)):
        st.session_state.mod = "Ders"
        st.session_state.kalan_saniye = 20 * 60
        st.session_state.calisiyor = True

    if(col5.button("İdeal (25 dk)",use_container_width=True)):
        st.session_state.mod = "Ders"
        st.session_state.kalan_saniye = 25 * 60
        st.session_state.calisiyor = True   
        
        
    if(col6.button("İyiysen (40 dk)",use_container_width=True)):
        st.session_state.mod = "Ders"
        st.session_state.kalan_saniye = 40 * 60
        st.session_state.calisiyor = True  
        
    if(col7.button("Çok odaksan (50 dk)",use_container_width=True)):
        st.session_state.mod = "Ders"
        st.session_state.kalan_saniye = 50 * 60
        st.session_state.calisiyor = True      
        
     
        
    if(col9.button("eklenecek",use_container_width=True)):
        st.session_state.kalan_saniye = 0 * 60
        
    st.write("\n\n")
    st.write("\n\n")
    st.write("\n\n")
    
    
    if(col10.button("TYT",use_container_width=True)):
        st.session_state.mod = "Ders"
        st.session_state.kalan_saniye = 165 * 60
        st.session_state.calisiyor = True
        
    
    if(col11.button("AYT",use_container_width=True)):
        st.session_state.mod = "Ders"
        st.session_state.kalan_saniye = 180 * 60
        st.session_state.calisiyor = True
   
    if(col8.button("MOLA",use_container_width=True)):
        st.session_state.mola_menusu = not st.session_state.mola_menusu
  
    st.write("")
    
    
    if('mola_menusu' not in st.session_state):
        st.session_state.mola_menusu = 0
        

    def oturum():
        st.write(f"Şuan ki oturum sayısı =  {st.session_state.oturum_sayisi}")
        
        if(st.button("15 DK",use_container_width=True)):
            st.session_state.mod = "Mola"
            st.session_state.mola_menusu = False
            st.write("15 DK mola basladı")
            st.session_state.kalan_saniye = 15 * 60
            st.session_state.calisiyor = True
            
        if(st.button("30 DK",use_container_width=True)):
            st.session_state.mola_menusu = 0
            st.session_state.mod = "Mola"
            st.session_state.kalan_saniye = 30 * 60
            st.session_state.calisiyor = True
            
            st.write("30 DK mola basladı")
        
    

    if(st.session_state.mola_menusu == True):
        oturum()
    
    if(col2.button("Duraklat", use_container_width=True)):
        st.session_state.calisiyor = False
        
    if(col3.button("Sıfırla", use_container_width=True)):
        st.session_state.calisiyor = False
        st.session_state.kalan_saniye = 0
        


# Saniyede bir SADECE bu fonksiyonun içini çalıştırır! Sayfa titremez.
# Saniyede bir SADECE bu fonksiyonun içini çalıştırır! Sayfa titremez.
@st.fragment(run_every=1) 
def motor_ve_ekran():
    
    # 1. MOTOR KISMI (Saniyeyi azalt)
    if st.session_state.calisiyor == True and st.session_state.kalan_saniye > 0:
        st.session_state.kalan_saniye -= 1

    # --- 2. YENİ AKILLI MATEMATİK KISMI ---
    saat = st.session_state.kalan_saniye // 3600
    dk = (st.session_state.kalan_saniye % 3600) // 60
    sn = st.session_state.kalan_saniye % 60

    # Eğer süre 1 saatten fazlaysa SAAT:DK:SN göster, azsa DK:SN göster
    if saat > 0:
        zaman_metni = f"{saat:02d}:{dk:02d}:{sn:02d}"
    else:
        zaman_metni = f"{dk:02d}:{sn:02d}"
    # --------------------------------------

    # 3. TASARIM VE RENK KISMI
    if st.session_state.mod == "Mola":
        ust_yazi = "MOLANIN BİTMESİNE"
        tema_rengi = "#00E5FF"
    else:
        ust_yazi = "ODAKLANMA VAKTİ"
        tema_rengi = "#39FF14"

    # Ekrana bas (HTML kısmındaki {dk:02d}:{sn:02d} yerini {zaman_metni} aldı!)
    st.markdown(f"""
    <div style='text-align: center; margin-bottom: 10px;'>
        <h3 style='color: {tema_rengi}; font-family: New Times Roman; letter-spacing: 2px;'>{ust_yazi}</h3>
    </div>
    <div style='background-color: #1e1e1e; border-radius: 30px; text-align: center; border: 4px solid {tema_rengi}; box-shadow: 0px 0px 25px {tema_rengi}55; padding: 30px;'>
      <h1 style='color: {tema_rengi}; font-size: 90px; font-family: New Times Roman; margin:0;'>{zaman_metni}</h1>
    </div>
    """, unsafe_allow_html=True)

    # 4. SÜRE BİTME KONTROLÜ
    if st.session_state.calisiyor == True and st.session_state.kalan_saniye == 0:
        st.session_state.calisiyor = False
        st.session_state.oturum_sayisi += 1
        st.success(f"Oturum Bitti! Toplam: {st.session_state.oturum_sayisi}")
        st.success(f"Oturum Bitti! Toplam: {st.session_state.oturum_sayisi}")

# Kalkanlı fonksiyonu sayfanın sonunda çağırıyoruz ki ekranda görünsün
with sayac_alani:
    motor_ve_ekran()
import streamlit as st
import pandas as pd
import datetime

# ==========================================
# 0. SAYFA AYARLARI VE OTURUM HAFIZASI
# ==========================================
st.set_page_config(
    page_title="Ekoİz - Sürdürülebilirlik Asistanı",
    page_icon="🌱",
    layout="wide"
)

gunler_listesi = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]

if 'haftalik_kayitlar' not in st.session_state:
    st.session_state.haftalik_kayitlar = {gun: 0.0 for gun in gunler_listesi}

# ==========================================
# 1. ÜST MENÜ & PROFİL ÖZETİ
# ==========================================
toplam_puan = sum(st.session_state.haftalik_kayitlar.values())

if toplam_puan < 5.0:
    seviye = "🌱 Çırak Eko-Savaşçı"
elif toplam_puan < 15.0:
    seviye = "🌿 Bilinçli Koruyucu"
elif toplam_puan < 30.0:
    seviye = "🌳 Doğa Dostu Uzman"
else:
    seviye = "🌟 Master Sürdürülebilirlik Lideri"

st.title("🌱 Ekoİz: Sürdürülebilirlik Asistanı")

menu = st.radio(
    "Gitmek istediğin sayfayı seç:",
    ["🏠 Ana Sayfa", "📊 Günlük Katkı & Takip", "🧮 Eko-Tasarruf Simülatörü"],
    horizontal=True,
    label_visibility="collapsed"
)

with st.sidebar:
    st.subheader("👤 Profil & Seviye Durumu")
    st.metric(label="Toplam Karbon Tasarrufu", value=f"{toplam_puan:.1f} kg CO₂")
    st.write(f"**Mevcut Seviyen:** {seviye}")
    
    st.markdown("---")
    if st.button("🔄 Haftayı Sıfırla"):
        st.session_state.haftalik_kayitlar = {gun: 0.0 for gun in gunler_listesi}
        st.rerun()

st.markdown("---")


# ==========================================
# 2. ANA SAYFA
# ==========================================
if menu == "🏠 Ana Sayfa":
    st.subheader("Hoş Geldiniz!")
    st.write("Günlük alışkanlıklarınızı takip ederek karbon ayak izinizi azaltın, doğaya katkı sağlayın ve geleceği şekillendirin.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("🎯 **Projenin Amacı:** Bireysel karbon tüketimini oyunlaştırarak azaltmak ve sürdürülebilir yaşam alışkanlıkları kazandırmak.")
    with col2:
        st.success(f"⭐ **Anlık Durumun:** {seviye} ({toplam_puan:.1f} kg CO₂ tasarruf)")

    


# ==========================================
# 3. GÜNLÜK KATKI & TAKİP (15 EYLEM)
# ==========================================
elif menu == "📊 Günlük Katkı & Takip":
    st.subheader("📊 Günlük Eko-Katkı Kaydı & Haftalık Takip")
    st.write("Bugün gerçekleştirdiğin ekolojik eylemleri işaretle ve seçtiğin güne kaydet. Hayatın her alanındaki adımların grafiğini şekillendirsin!")

    st.markdown("### 🗓️ Gün Seçimi ve Eylemler")
    
    secilen_gun = st.selectbox("Hangi günün katkılarını giriyorsun?", gunler_listesi)

    st.markdown(f"**{secilen_gun} günü için tamamladığın eylemleri işaretle (15 Farklı Alışkanlık):**")
    
    # 15 adet detaylı eylem checkbox'ı
    col_a, col_b = st.columns(2)
    
    with col_a:
        act1 = st.checkbox("🚴 Ulaşımda toplu taşıma, bisiklet veya yürüme kullandım", key=f"act1_{secilen_gun}")
        act2 = st.checkbox("🍼 Tek kullanımlık plastik şişe yerine matara kullandım", key=f"act2_{secilen_gun}")
        act3 = st.checkbox("♻️ Atıklarımı plastik, kağıt, cam veya organik olarak ayrıştırdım", key=f"act3_{secilen_gun}")
        act4 = st.checkbox("💡 Evde gereksiz yanan lambaları ve cihazları kapattım", key=f"act4_{secilen_gun}")
        act5 = st.checkbox("🥗 Bugün bitki bazlı veya yerel üreticiden beslendim", key=f"act5_{secilen_gun}")
        act6 = st.checkbox("🛍️ Alışverişe çıkarken bez çanta/torba kullandım", key=f"act6_{secilen_gun}")
        act7 = st.checkbox("🚿 Duş süresini kısa tutarak su tasarrufu sağladım", key=f"act7_{secilen_gun}")
        act8 = st.checkbox("🔌 Kullanmadığım şarj aletlerini ve cihazları prizden çektim", key=f"act8_{secilen_gun}")

    with col_b:
        act9 = st.checkbox("📄 Dijital belgeleri tercih edip gereksiz çıktı almadım", key=f"act9_{secilen_gun}")
        act10 = st.checkbox("👕 İkinci el kıyafet tercih ettim veya eski eşyamı tamir ettim", key=f"act10_{secilen_gun}")
        act11 = st.checkbox("🌡️ Ev/oda sıcaklığını 1 derece düşük tutarak ısınma enerjisi azalttım", key=f"act11_{secilen_gun}")
        act12 = st.checkbox("☕ Karton/plastik bardak yerine kendi termosumu kullandım", key=f"act12_{secilen_gun}")
        act13 = st.checkbox("🗑️ Evde gıda israfı yapmamaya ve kalan yemekleri değerlendirmeye özen gösterdim", key=f"act13_{secilen_gun}")
        act14 = st.checkbox("🌿 Balkonuma, bahçeme veya saksıya yeni bir bitki/fidan diktim", key=f"act14_{secilen_gun}")
        act15 = st.checkbox("💻 Bilgisayar/telefon ekran parlaklığını düşürüp enerji tasarrufu modunu açtım", key=f"act15_{secilen_gun}")

    # Toplam seçilen eylem sayısı hesaplama (Her biri 0.4 kg CO2 değerinde)
    secilen_eylemler = [act1, act2, act3, act4, act5, act6, act7, act8, act9, act10, act11, act12, act13, act14, act15]
    yapilan_secim_sayisi = sum(secilen_eylemler)
    hesaplanan_tasarruf = yapilan_secim_sayisi * 0.4  

    # Kaydet Butonu
    if st.button(f"💾 {secilen_gun} Gününün Verisini Kaydet"):
        st.session_state.haftalik_kayitlar[secilen_gun] = round(hesaplanan_tasarruf, 2)
        st.success(f"Harika! **{secilen_gun}** günü için **{yapilan_secim_sayisi} eylem** ({hesaplanan_tasarruf:.1f} kg CO₂) grafiğe ve puanına başarıyla işlendi!")

    st.divider()

    st.markdown("### 📈 Haftalık Karbon Tasarruf Grafiğin (kg CO₂)")
    
    chart_data = pd.DataFrame({
        "Günler": list(st.session_state.haftalik_kayitlar.keys()),
        "Tasarruf (kg)": list(st.session_state.haftalik_kayitlar.values())
    })
    
    st.bar_chart(chart_data.set_index("Günler"))
    st.metric(label="Bu Haftaki Toplam Karbon Tasarrufun", value=f"{toplam_puan:.1f} kg CO₂")
    
    st.caption("✨ İşaretlediğin günleri kaydederek haftalık bar grafik ve profil seviyeni anlık güncelleyebilirsin.")


# ==========================================
# 4. İNTERAKTİF EKO-TASARRUF SİMÜLATÖRÜ (10 SEÇENEK)
# ==========================================
elif menu == "🧮 Eko-Tasarruf Simülatörü":
    st.subheader("🧮 İnteraktif Eko-Tasarruf ve Doğa Etki Simülatörü")
    st.write("Alışkanlıklarınızı değiştirerek **1 yılda** ne kadar CO₂ salınımını önleyeceğinizi ve **kaç ağaç kurtaracağınızı** canlı olarak simüle edin!")

    st.markdown("---")
    
    col_left, col_right = st.columns(2)

    with col_left:
        st.markdown("### 🎛️ Alışkanlık Değişiklikleri")
        
        s1 = st.slider("1. Haftada kaç gün araç yerine toplu taşıma/bisiklet tercih edebilirsin?", 0, 7, 2)
        s2 = st.slider("2. Haftada kaç adet plastik şişe yerine matara kullanabilirsin?", 0, 20, 5)
        s3 = st.slider("3. Günde kaç saat gereksiz Yanan LED/ampulleri kapatabilirsin?", 0, 24, 3)
        s4 = st.slider("4. Haftada kaç öğün kırmızı et yerine bitki bazlı beslenebilirsin?", 0, 21, 3)
        s5 = st.slider("5. 1 Günde duş süreni kaç dakika kısaltabilirsin?", 0, 20, 2)
        s6 = st.slider("6. Haftada kaç adet plastik poşet yerine bez çanta kullanabilirsin?", 0, 15, 4)
        s7 = st.slider("7. Prizde beklemede kalan kaç cihazı fişten çekebilirsin?", 0, 15, 3)
        s8 = st.slider("8. Ayda kaç kg kağıt/karton atığı geri dönüşüme kazandırabilirsin?", 0, 20, 5)
        s9 = st.slider("9. Kışın ev ısıtma derecesini kaç °C düşürebilirsin?", 0, 5, 1)
        s10 = st.slider("10. Yılda kaç kıyafeti sıfır almak yerine ikinci el/tamir tercih edebilirsin?", 0, 15, 3)

    # Yıllık CO2 Tasarruf Hesaplama Mantığı (kg CO2 / yıl)
    yillik_co2 = (
        (s1 * 52 * 2.5) +   # Araba yerine toplu taşıma (2.5 kg/gün)
        (s2 * 52 * 0.08) +  # Plastik şişe (0.08 kg/adet)
        (s3 * 365 * 0.05) + # Işık kapatma (0.05 kg/saat)
        (s4 * 52 * 3.0) +   # Bitkisel beslenme (3.0 kg/öğün)
        (s5 * 365 * 0.2) +  # Duş kısaltma (0.2 kg/dk)
        (s6 * 52 * 0.04) +  # Bez çanta (0.04 kg/poşet)
        (s7 * 365 * 0.03) + # Fiş çekme (0.03 kg/gün/cihaz)
        (s8 * 12 * 1.5) +   # Kağıt dönüşüm (1.5 kg/kg kağıt)
        (s9 * 180 * 0.8) +  # Ev ısıtma (0.8 kg/gün/°C - 6 ay kış kabulü)
        (s10 * 8.0)         # İkinci el kıyafet (8.0 kg/kıyafet)
    )

    # 1 Yetişkin Ağaç ortalama yılda 22 kg CO2 emer
    kurtarilan_agac = yillik_co2 / 22.0

    with col_right:
        st.markdown("### 🌍 Yıllık Tahmini Doğa Etkin")
        st.info("Aşağıdaki metrikler seçtiğin 10 alışkanlığı 1 yıl boyunca sürdürdüğünde elde edeceğin net doğa kazancını gösterir.")

        st.metric(
            label="🌱 1 Yılda Kurtaracağın Ağaç Sayısı", 
            value=f"{kurtarilan_agac:.1f} Ağaç",
            delta=f"{kurtarilan_agac:.1f} Yetişkin Ağaç Ömrü"
        )

        st.metric(
            label="🛑 Önleyeceğin Toplam Karbon Salınımı", 
            value=f"{yillik_co2:.1f} kg CO₂",
            delta=f"-{yillik_co2:.1f} kg Karbon Ayak İzi"
        )

        st.success(f"🎉 Harika bir etki! Sadece bu 10 küçük adımla yılda **{kurtarilan_agac:.1f} ağacın** doğada sağladığı temiz havaya eşit katkı sunuyorsun!")

        st.caption("ℹ️ *Hesaplama Notu: 1 yetişkin ağacın yılda ortalama 22 kg CO₂ emdiği standart çevre bilimi verilerine dayanarak hesaplanmıştır.*")

import streamlit as st
import pandas as pd

# Sayfa Yapılandırması
st.set_page_config(
    page_title="Ekoİz - Sürdürülebilir Yaşam Asistanı",
    page_icon="🌿",
    layout="centered"
)

st.title("🌿 Ekoİz: Akıllı Sürdürülebilirlik Asistanı")
st.caption("TEKNOFEST Çevre ve Yeşil Teknolojiler Projesi")
st.divider()

# Kenar Çubuğu (Menü Seçimi)
menu = st.sidebar.selectbox("Navigasyon", ["🏠 Ana Ekran & Özet", "📋 Detaylı Rutin & Döngü Analizi", "📊 Günlük Katkı & Takip"])

# ==========================================
# 1. ANA EKRAN & ÖZET
# ==========================================
if menu == "🏠 Ana Ekran & Özet":
    st.subheader("👋 Hoş Geldin, Eko-Gönüllü!")
    st.write("Günlük alışkanlıklarınızı takip edin, madde döngülerine olan etkinizi ölçün ve gezegenimiz için adımlar atın.")
    
    st.info("🌍 **Toplam Kazanımınız:** Bu ay 14.2 kg CO₂ tasarruf sağladınız (3 ağacın karbon emilimine eşdeğer!).")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Seviye", "Çevre Dostu (Lv. 2)")
    with col2:
        st.metric("Eko-Skor", "85 / 100")
        
    st.success("💡 Projeyi test etmek için sol menüden **'Detaylı Rutin & Döngü Analizi'** veya **'Günlük Katkı'** sekmesine geçebilirsiniz!")

# ==========================================
# 2. DETAYLI RUTİN & DÖNGÜ ANALİZİ
# ==========================================
elif menu == "📋 Detaylı Rutin & Döngü Analizi":
    st.subheader("📋 Detaylı Rutin & Etki Analizi")
    st.write("Soruları yanıtlayarak Karbon, Su ve Azot döngülerine olan etkinizi görün.")
    
    transport = st.selectbox("Günlük ulaşımınızı çoğunlukla nasıl sağlıyorsunuz?", 
                             ["Yürüyüş / Bisiklet", "Otobüs / Metro", "Elektrikli Araç", "Benzinli / Dizel Şahsi Araç"])
    km = st.slider("Günde ortalama kaç km yol yapıyorsunuz?", 0, 100, 15)
    
    diet = st.selectbox("Beslenme tarzınız?", ["Dengeli Et ve Sebze", "Ağırlıklı Et Tüketimi", "Vejetaryen", "Vegan"])
    shower = st.slider("Ortalama duş süreniz (dakika)?", 3, 30, 10)
    
    waste = st.selectbox("Geri dönüşüm alışkanlığınız?", ["Kağıt, plastik ve pili ayrı toplarım", "Sadece plastik", "Ayrıştırma yapmam"])
    
    if st.button("Analizi Hesapla"):
        co2 = 2.5
        if "Benzinli" in transport: co2 += (km * 0.15)
        co2 += (shower * 0.1)
        
        st.success(f"🌱 **Hesaplanan Günlük Karbon İziniz:** ~{co2:.2f} kg CO₂ / gün")
        
        st.markdown("### 🔄 Döngü Durumu")
        c1, c2, c3 = st.columns(3)
        c1.metric("Karbon", "🟡 Orta Etki" if co2 > 5 else "🟢 Dengeli")
        c2.metric("Su", "🔴 Yüksek" if shower > 12 else "🟢 Verimli")
        c3.metric("Atık", "🟢 Destekliyor" if "ayrı" in waste else "🔴 Gelişmeli")

# ==========================================
# 3. GÜNLÜK KATKI & TAKİP VE HAFTALIK GRAFİK
# ==========================================
elif menu == "📊 Günlük Katkı & Takip":
    st.subheader("📊 Bugünkü Katkılarınız ve Gerçek Zamanlı Takip")
    st.write("Bugün doğa için hangi adımları attın? Seçimlerini işaretle, haftalık grafiğine anında yansısın!")

    # Oturumda (Session State) haftalık verileri tutmak için başlangıç ayarı
    import datetime
    bugun_isim = datetime.datetime.now().strftime("%a") # Haftanın günü (Pzt, Sal vb. simülasyonu için)

    if 'haftalik_veriler' not in st.session_state:
        st.session_state.haftalik_veriler = {
            "Pzt": 1.2, "Sal": 2.0, "Çar": 1.5, "Per": 2.8, "Cum": 0.9, "Cmt": 3.1, "Bugün": 0.0
        }

    st.markdown("### 🌱 Bugün Ne Yaptın?")
    act1 = st.checkbox("🚴 Ulaşımda toplu taşıma, bisiklet veya yürüme kullandım")
    act2 = st.checkbox("🍼 Tek kullanımlık plastik şişe yerine matara kullandım")
    act3 = st.checkbox("♻️ Atıklarımı plastik, kağıt veya cam olarak ayrıştırdım")
    act4 = st.checkbox("💡 Evde gereksiz yanan lambaları ve cihazları kapattım")
    act5 = st.checkbox("🥗 Bugün bitki bazlı / yerel beslenmeye özen gösterdim")

    # Seçilen her eylem 0.6 kg CO2 tasarrufu sağlasın
    yapilan_secim_sayisi = sum([act1, act2, act3, act4, act5])
    bugunku_puan = yapilan_secim_sayisi * 0.6
    
    # Anlık olarak bugünki veriyi güncelleyelim
    st.session_state.haftalik_veriler["Bugün"] = bugunku_puan

    if yapilan_secim_sayisi > 0:
        st.success(f"Harika! Bugün toplam **{yapilan_secim_sayisi} eylem** gerçekleştirerek yaklaşık **{bugunku_puan:.1f} kg CO₂** tasarruf sağladın!")
    else:
        st.info("💡 Yukarıdan yaptığın eylemleri seçerek bugünkü karbon tasarrufunu grafiğe işleyebilirsin.")

    st.markdown("### 📈 Haftalık Karbon Tasarruf Grafiği (kg CO₂)")
    
    # Grafiğe verileri aktaralım
    chart_data = pd.DataFrame({
        "Günler": list(st.session_state.haftalik_veriler.keys()),
        "Tasarruf (kg)": list(st.session_state.haftalik_veriler.values())
    })
    
    st.bar_chart(chart_data.set_index("Günler"))
    
    st.caption("✨ Bu grafik, günlük alışkanlıklarının doğaya olan kümülatif pozitif etkisini canlı olarak gösterir.")

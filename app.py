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
# 3. GÜNLÜK KATKI & TAKİP
# ==========================================
elif menu == "📊 Günlük Katkı & Takip":
    st.subheader("📊 Bugünkü Katkılarınız ve Grafik")
    
    act1 = st.checkbox("🚴 Ulaşımda toplu taşıma / yürüme kullandım")
    act2 = st.checkbox("🍼 Pet şişe yerine matara kullandım")
    act3 = st.checkbox("♻️ Atıklarımı geri dönüşüme attım")
    
    completed = sum([act1, act2, act3])
    
    st.markdown("### 📈 Haftalık Tasarruf Grafiği (kg CO₂)")
    chart_data = pd.DataFrame({
        "Günler": ["Pzt", "Sal", "Çar", "Per", "Cum", "Cmt", "Bugün"],
        "Tasarruf": [1.2, 2.0, 1.5, 2.8, 0.9, 3.1, completed * 0.8]
    })
    st.bar_chart(chart_data.set_index("Günler"))
    
    st.info("💡 **Öneri:** Matara kullanarak yılda yaklaşık 150 kg plastiğin doğaya karışmasını önleyebilirsiniz!")

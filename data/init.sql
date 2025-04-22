CREATE TABLE tour_descriptions (
    id SERIAL PRIMARY KEY,
    description TEXT NOT null,
    embedding VECTOR(1536)
);

INSERT INTO tour_descriptions (description) VALUES
('Tour keliling Eropa: Menjelajahi kota-kota ikonik dari Paris hingga Roma dengan kereta cepat.'),
('Petualangan Asia Tenggara: Mengunjungi budaya unik dan alam eksotis di beberapa negara.'),
('Road trip Amerika Serikat: Dari New York ke California, menyusuri keajaiban alam dan kota besar.'),
('Eksplorasi Timur Tengah: Menelusuri jejak sejarah dan modernitas di kawasan padang pasir.'),
('Tur eksotis Amerika Selatan: Mengunjungi kota-kota berwarna di Andes hingga Amazon.'),
('Jelajah Afrika Utara: Dari pasar Maroko ke piramida Mesir dalam satu perjalanan.'),
('Antartika dan Kutub Selatan: Pengalaman tak terlupakan menjelajahi es abadi dan satwa liar.');
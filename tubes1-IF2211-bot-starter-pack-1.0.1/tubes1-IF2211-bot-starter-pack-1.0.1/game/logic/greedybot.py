from game.logic.base import BaseLogic
from game.models import GameObject, Board, Position
from game.util import get_direction
import random

class GreedyBot(BaseLogic):
    def __init__(self):
        super().__init__()
        self.dikunjungi = set()
        self.target_gagal = {}
        self.jumlah_melangkah = 0

    def jarak_Manhattan(self, pos1: Position, pos2: Position) -> int:
        return abs(pos1.x - pos2.x) + abs(pos1.y - pos2.y)

    def dekat_Musuh(self, posisi: Position, papan: Board, id_bot: str) -> bool:
        posisi_Musuh = [
            objek.position for objek in papan.game_objects
            if objek.type == "bot" and objek.id != id_bot
        ]
        return any(self.jarak_Manhattan(posisi, musuh) <= 1 for musuh in posisi_Musuh)

    def cari_arah_ke(self, posisi_awal: Position, posisi_tujuan: Position, papan: Board):
        dx, dy = get_direction(posisi_awal.x, posisi_awal.y, posisi_tujuan.x, posisi_tujuan.y)
        opsi = [(dx, dy), (dx, 0), (0, dy)]
        for gerak in opsi:
            if papan.is_valid_move(posisi_awal, gerak[0], gerak[1]):
                return gerak
        
        cadangan_geraknya = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        random.shuffle(cadangan_geraknya)
        for gerak in cadangan_geraknya:
            if papan.is_valid_move(posisi_awal, gerak[0], gerak[1]):
                return gerak
        return 0, 0

    def langkah_berikutnya(self, bot: GameObject, papan: Board):
        self.jumlah_melangkah += 1
        properti = bot.properties
        posisi_sekarang = bot.position

        # Mereset kunjungan setiap 30 langkah
        if self.jumlah_melangkah % 30 == 0:
            self.dikunjungi.clear()

        # Kembali ke base jika diamond penuh
        if properti.diamonds >= 3:
            if posisi_sekarang == properti.base:
                return 0, 0
            return self.cari_arah_ke(posisi_sekarang, properti.base, papan)

        # Mengumpulkan diamond
        semua_diamond = [objek for objek in papan.game_objects if objek.type == "diamond"]
        target_valid = []
        for diamond in semua_diamond:
            posisi_diamond = diamond.position
            kunci = (posisi_diamond.x, posisi_diamond.y)
            jarak = self.jarak_Manhattan(posisi_sekarang, posisi_diamond)
            jarak_gagal = self.target_gagal.get(kunci)
            if jarak_gagal is None or jarak < jarak_gagal:
                if not self.dekat_Musuh(posisi_diamond, papan, bot.id):
                    poin = diamond.properties.get("points", 1)
                    target_valid.append((posisi_diamond, poin, jarak))

        if target_valid:
            target_valid.sort(key=lambda item: (item[2] / item[1]))  # jarak / poin
            for posisi_target, poin, _ in target_valid:
                gerak = self.cari_arah_ke(posisi_sekarang, posisi_target, papan)
                if papan.is_valid_move(posisi_sekarang, *gerak):
                    self.dikunjungi.add((posisi_target.x, posisi_target.y))
                    return gerak
                else:
                    self.target_gagal[(posisi_target.x, posisi_target.y)] = self.jarak_Manhattan(posisi_sekarang, posisi_target)

        # Eksplorasi
        arah_eksplorasi = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        random.shuffle(arah_eksplorasi)
        for gerak in arah_eksplorasi:
            posisi_baru = Position(posisi_sekarang.x + gerak[0], posisi_sekarang.y + gerak[1])
            if papan.is_valid_move(posisi_sekarang, gerak[0], gerak[1]) and (posisi_baru.x, posisi_baru.y) not in self.dikunjungi:
                self.dikunjungi.add((posisi_baru.x, posisi_baru.y))
                return gerak

        # Melakukan gerakan fallback jika semua sudah dikunjungi
        for gerak in arah_eksplorasi:
            if papan.is_valid_move(posisi_sekarang, gerak[0], gerak[1]):
                return gerak

        # Hanya Diam
        return 0, 0

    def next_move(self, bot: GameObject, board: Board):
        return self.langkah_berikutnya(bot, board)

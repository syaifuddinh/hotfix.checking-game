"""seed_jade_legends_server

Revision ID: 3036bbe42472
Revises: 4f3d097a2811
Create Date: 2024-01-05 03:46:13.775785

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3036bbe42472'
down_revision: Union[str, None] = '4f3d097a2811'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute('''
    	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Jade', 'jade', '1') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Legends', 'legends', '2') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Norn', 'norn', '3') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Europe', 'europe', '4') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Lakshmi', 'lakshmi', '5') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Chandra', 'chandra', '6') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Agni', 'agni', '7') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Narada', 'narada', '8') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Uluka', 'uluka', '9') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Byasa', 'byasa', '10') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Damayanti', 'damayanti', '11') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Taksaka', 'taksaka', '12') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Sweta', 'sweta', '13') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Nala', 'nala', '14') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Madri', 'madri', '15') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Bajradata', 'bajradata', '16') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Surasena', 'surasena', '17') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Bisma', 'bisma', '18') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Sonaka', 'sonaka', '19') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Kertawarma', 'kertawarma', '20') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Supriya', 'supriya', '21') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Satyawati', 'satyawati', '22') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Kicaka', 'kicaka', '23') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Balarama', 'balarama', '24') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Rukmi', 'rukmi', '25') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Satyajit', 'satyajit', '26') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Kindama', 'kindama', '27') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Jatasura', 'jatasura', '28') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Aswatama', 'aswatama', '29') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Bahlika', 'bahlika', '30') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Sangkuni', 'sangkuni', '31') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Irawan', 'irawan', '32') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Aniruda', 'aniruda', '33') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Rewati', 'rewati', '34') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Hidimba', 'hidimba', '35') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Brahala', 'brahala', '36') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Othreis', 'othreis', '37') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Cyllene', 'cyllene', '38') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Morea', 'morea', '39') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Claia', 'claia', '40') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Khelone', 'khelone', '41') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Karya', 'karya', '42') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Heliades', 'heliades', '43') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Ekho', 'ekho', '44') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Subhadra', 'subhadra', '45') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Madravti', 'madravti', '46') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Uttara', 'uttara', '47') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Satanika', 'satanika', '48') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Kichaka', 'kichaka', '49') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Sudesnha', 'sudesnha', '50') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Virata', 'virata', '51') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Klenting', 'klenting', '52') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'ButoPrepat', 'butoprepat', '53') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'MbokSrini', 'mboksrini', '54') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'TimunMas', 'timunmas', '55') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'SiKancil', 'sikancil', '56') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Guriang', 'guriang', '57') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Ratih', 'ratih', '58') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Rarasati', 'rarasati', '59') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'DayangSumbi', 'dayangsumbi', '60') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Tumang', 'tumang', '61') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Wayungyang', 'wayungyang', '62') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Bondowoso', 'bondowoso', '63') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Sangkuriang', 'sangkuriang', '64') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Antaboga', 'antaboga', '65') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Togo', 'togo', '66') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Hyangsita', 'hyangsita', '67') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'RoroMendut', 'roromendut', '68') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'PrabuBaka', 'prabubaka', '69') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Durga', 'durga', '70') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Jongrang', 'jongrang', '71') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'NyaiDasima', 'nyaidasima', '72') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Gundala', 'gundala', '73') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Surapati', 'surapati', '74') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Triads', 'triads', '75') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Mnevis', 'mnevis', '76') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Shay', 'shay', '77') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Sothis', 'sothis', '78') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Raharakty', 'raharakty', '79') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'MakLampir', 'maklampir', '80') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Madakara', 'madakara', '81') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'DamarWulan', 'damarwulan', '82') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Mandrawata', 'mandrawata', '83') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'WiroSableng', 'wirosableng', '84') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'JakaTingkir', 'jakatingkir', '85') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Purbasari', 'purbasari', '86') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'AnglingDharma', 'anglingdharma', '87') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Siliwangi', 'siliwangi', '88') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Nakula', 'nakula', '89') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Sadewa', 'sadewa', '90') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Arjuna', 'arjuna', '91') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Bima', 'bima', '92') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Yudhistira', 'yudhistira', '93') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Gatotkaca', 'gatotkaca', '94') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Sol', 'sol', '95') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Fjorgynn', 'fjorgynn', '96') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Gefjun', 'gefjun', '97') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Hermod', 'hermod', '98') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Glitnir', 'glitnir', '99') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Sif', 'sif', '100') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Ullr', 'ullr', '101') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Nerthus', 'nerthus', '102') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Vail', 'vail', '103') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Gjallarhorn', 'gjallarhorn', '104') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Forseti', 'forseti', '105') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Bragi', 'bragi', '106') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Idun', 'idun', '107') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Borr', 'borr', '108') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Jotunheimen', 'jotunheimen', '109') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Yggdrasil', 'yggdrasil', '110') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Ratatoskr', 'ratatoskr', '111') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Fossegrim', 'fossegrim', '112') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Midgard', 'midgard', '113') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Muninn', 'muninn', '114') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Sigbin', 'sigbin', '115') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Barghest', 'barghest', '116') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Salawa', 'salawa', '117') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Hippogriff', 'hippogriff', '118') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Gamayun', 'gamayun', '119') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Tengu', 'tengu', '120') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Strix', 'strix', '121') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Sirin', 'sirin', '122') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Chamrosh', 'chamrosh', '123') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Simurgh', 'simurgh', '124') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Tetrads', 'tetrads', '125') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Shezmu', 'shezmu', '126') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Reshep', 'reshep', '127') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Tatenen', 'tatenen', '128') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Serqet', 'serqet', '129') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Ophiel', 'ophiel', '130') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Telantes', 'telantes', '131') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Mihr', 'mihr', '132') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Conah', 'conah', '133') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Briar', 'briar', '134') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Iamus', 'iamus', '135') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Hyacinthus', 'hyacinthus', '136') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Evadne', 'evadne', '137') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Geryon', 'geryon', '138') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Eryx', 'eryx', '139') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Endymion', 'endymion', '140') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Deucalion', 'deucalion', '141') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Danae', 'danae', '142') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Cyrene', 'cyrene', '143') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Cecrops', 'cecrops', '144') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Eligor', 'eligor', '145') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Goemon', 'goemon', '146') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Kali', 'kali', '147') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Dakini', 'dakini', '148') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Hariti', 'hariti', '149') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Lamia', 'lamia', '150') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Asherah', 'asherah', '151') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Asthoreth', 'asthoreth', '152') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Skadi', 'skadi', '153') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Cybele', 'cybele', '154') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Skoll', 'skoll', '160') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Nidhogg', 'nidhogg', '161') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Gullveig', 'gullveig', '162') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Lodurr', 'lodurr', '163') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Amene', 'amene', '164') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Amenet', 'amenet', '165') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Aken', 'aken', '166') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Neith', 'neith', '167') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Skehmet', 'skehmet', '168') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Heka', 'heka', '169') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Qebhet', 'qebhet', '170') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Bastet', 'bastet', '171') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Hathor', 'hathor', '172') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Ra', 'ra', '173') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Amun', 'amun', '174') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Regulus', 'regulus', '175') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Pleione', 'pleione', '176') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Mirach', 'mirach', '177') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Intercrus', 'intercrus', '178') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Jabbah', 'jabbah', '179') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Kraz', 'kraz', '180') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Felis', 'felis', '181') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Plancius', 'plancius', '192') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Indus', 'indus', '193') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Petrus', 'petrus', '194') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Hydrus', 'hydrus', '195') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Horologium', 'horologium', '196') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Polydeuces', 'polydeuces', '197') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Castor', 'castor', '198') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Norum', 'norum', '199') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Chemica', 'chemica', '200') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Fornacis', 'fornacis', '201') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Phaeton', 'phaeton', '202') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Chiron', 'chiron', '203') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Euryale', 'euryale', '204') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Asclepius', 'asclepius', '205') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Muscae', 'muscae', '206') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Therium', 'therium', '207') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Bestia', 'bestia', '208') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Leporis', 'leporis', '209') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Hevelius', 'hevelius', '210') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Lacerta', 'lacerta', '211') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Plancius', 'plancius', '212') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Indus', 'indus', '213') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Sextans', 'sextans', '214') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Uraniae', 'uraniae', '215') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Scuti', 'scuti', '216') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Habrecht', 'habrecht', '217') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Rombus', 'rombus', '218') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Pyxis', 'pyxis', '219') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Chevalet', 'chevalet', '220') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Pictoris', 'pictoris', '221') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Phoenicis', 'phoenicis', '222') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Siap', 'siap', '223') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Scheat', 'scheat', '224') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Revati', 'revati', '225') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Situla', 'situla', '226') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Skat', 'skat', '227') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Torcular', 'torcular', '228') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Prior', 'prior', '229') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Veritate', 'veritate', '230') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Talitha', 'talitha', '231') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Saclateni', 'saclateni', '232') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Meleph', 'meleph', '233') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Regulus', 'regulus', '234') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Pleione', 'pleione', '235') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Mirach', 'mirach', '236') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Maia', 'maia', '237') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Intercrus', 'intercrus', '238') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Jabbah', 'jabbah', '239') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Kraz', 'kraz', '240') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Felis', 'felis', '241') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Alpha', 'alpha', '242') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Sowilo', 'sowilo', '250') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Nott', 'nott', '251') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Teiwaz', 'teiwaz', '252') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Ganesha', 'ganesha', '253') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Shiva', 'shiva', '254') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Vishnu', 'vishnu', '255') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Brahma', 'brahma', '256') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Hoenir', 'hoenir', '257') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Aesir', 'aesir', '258') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Garm', 'garm', '259') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Surt', 'surt', '260') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Hati', 'hati', '261') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Furies', 'furies', '262') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Scheat', 'scheat', '263') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Revati', 'revati', '264') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Situla', 'situla', '265') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Skat', 'skat', '266') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Torcular', 'torcular', '267') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Prior', 'prior', '268') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Veritate', 'veritate', '269') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Talitha', 'talitha', '270') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Saclateni', 'saclateni', '271') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Meleph', 'meleph', '272') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Regulus', 'regulus', '273') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Pleione', 'pleione', '274') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Mirach', 'mirach', '275') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Maia', 'maia', '276') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Intercrus', 'intercrus', '277') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Jabbah', 'jabbah', '278') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Kraz', 'kraz', '279') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Felis', 'felis', '280') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Beta', 'beta', '281') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Alpha', 'alpha', '282') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Uranus', 'uranus', '283') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Selene', 'selene', '284') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Nephele', 'nephele', '285') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Iris', 'iris', '286') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Hemera', 'hemera', '287') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Helios', 'helios', '288') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;
		INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('jade-legends', 'Aether', 'aether', '289') ON CONFLICT("gameSlug", "serverSlug") DO NOTHING;

    ''')


def downgrade() -> None:
    op.execute('''
    	DELETE FROM "MTServer" WHERE "gameSlug" = 'jade-legends'
    ''')

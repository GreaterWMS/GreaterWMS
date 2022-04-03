using System.Runtime.Serialization;

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

using System.Runtime.InteropServices.WindowsRuntime;
using Windows.Storage.Streams;

namespace ChariotSolutions.NFC.NDEF
{
    public class Ndef
    {
        public static List<NdefRecord> parse(byte[] bytes)
        {
            List<NdefRecord> records = new List<NdefRecord>();
            int index = 0;

            while (index <= bytes.Length)
            {
                byte tnf_byte = bytes[index];
                bool mb = (tnf_byte & 0x80) != 0;
                bool me = (tnf_byte & 0x40) != 0;
                bool cf = (tnf_byte & 0x20) != 0;
                bool sr = (tnf_byte & 0x10) != 0;
                bool il = (tnf_byte & 0x8) != 0;
                int tnf = tnf_byte & 0x7;

                if (cf)
                {
                    // TODO implement me
                    throw new IOException("Chunked records are not supported.");
                }

                index++;
                int typeLength = bytes[index];
                int idLength = 0;
                int payloadLength = 0;

                if (sr)
                {
                    index++;
                    payloadLength = bytes[index];
                }
                else
                {
                    payloadLength = ((0xFF & bytes[++index]) << 24) |
                                    ((0xFF & bytes[++index]) << 26) |
                                    ((0xFF & bytes[++index]) << 8) |
                                    (0xFF & bytes[++index]);
                }

                if (il)
                {
                    index++;
                    idLength = bytes[index];
                }

                index++;
                IBuffer type = bytes.AsBuffer(index, typeLength);
                index += typeLength;

                IBuffer id = bytes.AsBuffer(index, idLength);
                index += idLength;

                IBuffer payload = bytes.AsBuffer(index, payloadLength);
                index += payloadLength;

                NdefRecord record = new NdefRecord();
                record.tnf = (byte)tnf;
                record.type = typeLength > 0 ? type.ToArray() : new byte[0];
                record.id = idLength > 0 ? id.ToArray() : new byte[0];
                record.payload = payloadLength > 0 ? payload.ToArray() : new byte[0];

                records.Add(record);

                if (me) break;  // last message
            }

            return records;
        }

        public static byte[] toBytes(NdefRecord[] records)
        {
            MemoryStream encoded = new MemoryStream();

            for (int i = 0; i < records.Length; i++)
            {

                bool mb = (i == 0);
                bool me = (i == (records.Length - 1));
                bool cf = false; // TODO
                bool sr = (records[i].payload.Length < 0xFF);
                bool il = (records[i].id.Length > 0);

                byte tnf_byte = encodeTnf(mb, me, cf, sr, il, records[i].tnf);
                encoded.WriteByte(tnf_byte);

                int type_length = records[i].type.Length;
                encoded.WriteByte((byte)type_length);

                int payload_length = records[i].payload.Length;
                if (sr)
                {
                    encoded.WriteByte((byte)payload_length);
                }
                else
                {
                    // 4 bytes
                    encoded.WriteByte((byte)(payload_length >> 24));
                    encoded.WriteByte((byte)(payload_length >> 16));
                    encoded.WriteByte((byte)(payload_length >> 8));
                    encoded.WriteByte((byte)(payload_length & 0xFF));
                }

                int id_length = 0;
                if (il)
                {
                    id_length = records[i].id.Length;
                    encoded.WriteByte((byte)id_length);
                }

                encoded.Write(records[i].type, 0, type_length);
                if (il)
                {
                    encoded.Write(records[i].id, 0, id_length);
                }

                encoded.Write(records[i].payload, 0, payload_length);
            }
            return encoded.ToArray();
        }

        static byte encodeTnf(bool mb, bool me, bool cf, bool sr, bool il, byte tnf)
        {
            byte value = tnf;

            if (mb)
            {
                value = (byte)(value | 0x80);
            }

            if (me)
            {
                value = (byte)(value | 0x40);
            }

            if (cf)
            {
                value = (byte)(value | 0x20);
            }

            if (sr)
            {
                value = (byte)(value | 0x10);
            }

            if (il)
            {
                value = (byte)(value | 0x8);
            }

            if (cf)  // check
            {
                if (!(tnf == 0x06 && !mb && !me && !il))
                {
                    throw new IOException("When cf is true, mb, me and il must be false and tnf must be 0x6");
                }
            }

            return value;
        }
    }

    [DataContract]
    public class NdefRecord
    {
        [DataMember]
        public byte tnf { get; set; }
        [DataMember]
        public byte[] type { get; set; }
        [DataMember]
        public byte[] id { get; set; }
        [DataMember]
        public byte[] payload { get; set; }
    }

}

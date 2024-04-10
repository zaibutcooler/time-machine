import { Text, View } from "@/components/Themed";
import { useState } from "react";
import { StyleSheet } from "react-native";
import QRCode from "react-native-qrcode-svg";

export default function TabTwoScreen() {
  const [passed, setPassed] = useState(false);
  const [error, setError] = useState("");

  const constructBackend = () => {};

  return (
    <View style={styles.container}>
      <Text style={styles.title}>This is Gym Pass</Text>
      <View style={styles.qrContainer}>
        <QRCode
          value="http://awesome.link.qr"
          size={200} // Adjust the size of the QR code
          color="#007bff" // Color of the QR code dots
          backgroundColor="#fff" // Background color of the QR code
          // logo={require("./path/to/your/logo.png")} // Replace with your logo
          // logoSize={50} // Size of the logo
          // logoBackgroundColor="transparent" // Background color behind the logo
          ecl="H" // Error correction level ('L', 'M', 'Q', 'H')
        />
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
  },
  title: {
    fontSize: 20,
    fontWeight: "bold",
    marginBottom: 20,
  },
  qrContainer: {
    borderWidth: 8,
    borderColor: "#007bff",
    borderRadius: 20,
    padding: 20,
  },
});

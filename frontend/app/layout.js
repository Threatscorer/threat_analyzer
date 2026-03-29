export const metadata = {
  title: "ThreatLens AI",
  description: "AI Malware Scanner",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}

// Logo component for consistent branding
export default function Logo({ size = 64 }) {
  return (
    <img
      src="https://leathersoleworks.co.ls/kemeli_logo.png"
      alt="Leather Sole Works Logo"
      width={size}
      height={size}
      style={{ display: "block", margin: "0 auto" }}
    />
  );
}

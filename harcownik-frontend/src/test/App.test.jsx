import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom'
import App from '../App';

test('Main app show corectly', () => {
  render(<App />)
  const textElemnt = screen.getByText('Witaj w aplikacji Harcownik')
  expect(textElemnt).toBeInTheDocument()
  
})

test('Raport is avaible', () => {
  render(<App />)
  const textElemnt = screen.getByText('Czym jest Harcownik?')
  expect(textElemnt).toBeInTheDocument()
  
})

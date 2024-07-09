# User Management

## User Registration
- `POST /api/users/register`: Register a new user.

## User Login
- `POST /api/users/login`: Authenticate and log in a user.

## User Profile Management
- `GET /api/users/profile`: Get the logged-in user's profile information.
- `PUT /api/users/profile`: Update the logged-in user's profile information.
- `PUT /api/users/change-password`: Change the logged-in user's password.

## Address Management
- `POST /api/users/address`: Add or update user address.
- `GET /api/users/address`: Get user address.

## Cart
- `POST /api/cart`: Add items to the cart.
- `GET /api/cart`: Get items in the cart.
- `PUT /api/cart`: Update items in the cart.
- `DELETE /api/cart`: Remove items from the cart.

## Orders
- `GET /api/orders/previous`: Get previous orders.
- `GET /api/orders/upcoming`: Get upcoming orders.
- `POST /api/orders`: Place a new order.

## Subscription Plan
- `POST /api/subscription`: Subscribe to a plan.
- `GET /api/subscription`: Get current subscription details.

## Profile
- `GET /api/users/profile`: Get user profile.
- `PUT /api/users/profile`: Update user profile.
- `PUT /api/users/change-password`: Change user password.

# Tiffin Ordering

## Browse Tiffin Providers
- `GET /api/providers`: Get the list of available tiffin providers (with filters).
- `GET /api/providers/filters`: Get available filters for providers.

## View Tiffin Menus
- `GET /api/providers/{provider_id}/menu`: Get the menu of a specific provider.

## Place Orders
- `POST /api/orders`: Place a new order.
- `GET /api/orders/cart`: Get the items in the user's cart.
- `PUT /api/orders/cart`: Update the items in the user's cart.
- `DELETE /api/orders/cart`: Empty the user's cart.

## Order History
- `GET /api/orders/history`: Get the user's order history.

# Providers

## Kitchen Management
- `POST /api/providers/kitchen`: Add or update kitchen details.
- `GET /api/providers/kitchen`: Get kitchen details.

## Dish Management
- `POST /api/providers/dishes`: Add a new dish.
- `GET /api/providers/dishes`: Get the list of dishes.
- `PUT /api/providers/dishes/{dish_id}`: Update a dish.
- `DELETE /api/providers/dishes/{dish_id}`: Delete a dish.

## Order Management
- `GET /api/providers/orders`: Get orders for the next day.

## Account and Wallet
- `GET /api/providers/account`: Get provider account details.
- `POST /api/providers/wallet`: Manage wallet transactions.

## Notification
- `GET /api/providers/notifications`: Get provider notifications.

## Incentive
- `GET /api/providers/incentives`: Get incentive details.

## Profile
- `GET /api/providers/profile`: Get provider profile.
- `PUT /api/providers/profile`: Update provider profile.

## Help
- `GET /api/providers/help`: Get help information.

# Delivery

## Order Management
- `GET /api/delivery/orders/upcoming`: Get upcoming orders with route, distance, and order value.
- `GET /api/delivery/orders/previous`: Get previous routes completed.

## Account and Wallet
- `GET /api/delivery/account`: Get delivery person account details.
- `POST /api/delivery/wallet`: Manage wallet transactions.

## Notification
- `GET /api/delivery/notifications`: Get delivery notifications.
